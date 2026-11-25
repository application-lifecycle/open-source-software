#!/usr/bin/env python3
"""Update open-source-software metadata from GitHub and rebuild README tables.

Usage:
  python3 scripts/update-directory.py --fetch-github --check-links
  python3 scripts/update-directory.py --render-only
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "data" / "software.json"
README_PATH = ROOT / "README.md"
USER_AGENT = "open-source-software-directory-bot/1.0"


def format_stars(stars: int | None) -> str:
    if stars is None:
        return "-"
    if stars >= 1000:
        return f"{stars / 1000:.1f}k"
    return str(stars)


def github_get(url: str, token: str | None) -> dict[str, Any] | None:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": USER_AGENT,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        print(f"GitHub HTTP {exc.code} for {url}", file=sys.stderr)
        return None
    except Exception as exc:
        print(f"GitHub request error for {url}: {exc}", file=sys.stderr)
        return None


def compute_status(archived: bool, last_pushed: str | None) -> str:
    if archived:
        return "Archived"
    if not last_pushed:
        return "Active"
    try:
        pushed_date = dt.date.fromisoformat(last_pushed[:10])
    except ValueError:
        return "Active"
    days = (dt.date.today() - pushed_date).days
    if days <= 120:
        return "Active"
    if days <= 365:
        return "Maintained"
    return "Slow"


def enrich_github_entry(entry: dict[str, Any], token: str | None) -> dict[str, Any]:
    repo = entry.get("github")
    if not repo:
        entry.setdefault("stars", None)
        entry.setdefault("status", "Active")
        return entry

    repo_data = github_get(f"https://api.github.com/repos/{repo}", token)
    if not repo_data:
        return entry

    entry["stars"] = repo_data.get("stargazers_count")
    pushed_at = repo_data.get("pushed_at")
    entry["last_pushed"] = pushed_at[:10] if pushed_at else entry.get("last_pushed")
    archived = bool(repo_data.get("archived", False))
    entry["status"] = compute_status(archived, entry.get("last_pushed"))

    lic = repo_data.get("license")
    if isinstance(lic, dict):
        spdx = lic.get("spdx_id")
        if spdx and spdx not in ("NOASSERTION", "OTHER"):
            entry["github_license"] = spdx

    rel_data = github_get(f"https://api.github.com/repos/{repo}/releases/latest", token)
    if rel_data and rel_data.get("published_at"):
        entry["last_release"] = rel_data["published_at"][:10]
        if rel_data.get("tag_name"):
            entry["latest_tag"] = rel_data["tag_name"]

    return entry


def check_url(url: str) -> tuple[bool, int | str]:
    headers = {"User-Agent": USER_AGENT}
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                return (200 <= resp.status < 400), resp.status
        except urllib.error.HTTPError as exc:
            # 403/405 on HEAD often means bot protection or HEAD disallowed.
            if method == "HEAD" and exc.code in (403, 405, 429):
                continue
            if exc.code in (403, 429):
                return True, exc.code
            return False, exc.code
        except Exception as exc:
            if method == "HEAD":
                continue
            return False, str(exc)
    return False, "unknown"


def replace_section(content: str, marker: str, body: str) -> str:
    pattern = re.compile(
        rf"(<!-- START:{re.escape(marker)} -->).*?(<!-- END:{re.escape(marker)} -->)",
        re.DOTALL,
    )
    replacement = f"\\1\n{body.strip()}\n\\2"
    new_content, count = pattern.subn(replacement, content)
    if count == 0:
        raise ValueError(f"Marker {marker} not found")
    return new_content


def software_link(item: dict[str, Any]) -> str:
    return f"[{item['name']}]({item['url']})"


def render_featured_table(data: dict[str, Any]) -> str:
    by_id = {item["id"]: item for item in data["software"]}
    lines = [
        "| Software | Alternative to | Platform | License | Best for | Migration |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item_id in data.get("featured", []):
        item = by_id.get(item_id)
        if not item:
            continue
        platforms = ", ".join(item["platforms"])
        lines.append(
            f"| {software_link(item)} | {item['alternative_to']} | {platforms} | "
            f"{item['license']} | {item['best_for']} | {item['migration']} |"
        )
    return "\n".join(lines)


def render_toc(data: dict[str, Any]) -> str:
    counts: dict[str, int] = {}
    for item in data["software"]:
        counts[item["category"]] = counts.get(item["category"], 0) + 1
    lines = []
    for cat in data["categories"]:
        anchor = re.sub(r"[^a-z0-9\s-]", "", cat["name"].lower()).strip()
        anchor = anchor.replace(" ", "-")
        count = counts.get(cat["id"], 0)
        lines.append(f"- [{cat['name']}](#{anchor}) ({count})")
    return "\n".join(lines)


def render_category_table(items: list[dict[str, Any]], include_release: bool = False) -> str:
    if include_release:
        lines = [
            "| Software | Alternative to | Platform | License | Stars | Last release | Activity | Migration | Best for |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    else:
        lines = [
            "| Software | Alternative to | Platform | License | Stars | Activity | Migration | Best for |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]

    for item in items:
        platforms = ", ".join(item["platforms"])
        stars = format_stars(item.get("stars"))
        status = item.get("status", "Active")
        lic = item["license"]
        if item.get("open_core") and "open-core" not in lic.lower():
            lic = f"{lic} *"
        if include_release:
            rel = item.get("last_release") or item.get("last_pushed") or "-"
            lines.append(
                f"| {software_link(item)} | {item['alternative_to']} | {platforms} | "
                f"{lic} | {stars} | {rel} | {status} | {item['migration']} | {item['best_for']} |"
            )
        else:
            lines.append(
                f"| {software_link(item)} | {item['alternative_to']} | {platforms} | "
                f"{lic} | {stars} | {status} | {item['migration']} | {item['best_for']} |"
            )
    return "\n".join(lines)


def render_catalog(data: dict[str, Any]) -> str:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in data["software"]:
        grouped.setdefault(item["category"], []).append(item)

    sections = []
    for cat in data["categories"]:
        items = grouped.get(cat["id"], [])
        header = f"### {cat['name']}\n\n{cat['summary']}"
        if cat.get("detail_page"):
            header += f" See the [detailed {cat['name']} notes]({cat['detail_page']})."
        table = render_category_table(items, include_release=False)
        sections.append(f"{header}\n\n{table}")
    return "\n\n".join(sections)


def render_stats(data: dict[str, Any]) -> str:
    total = len(data["software"])
    cats = len(data["categories"])
    open_core_count = sum(1 for item in data["software"] if item.get("open_core"))
    updated = data["metadata"].get("last_updated", dt.date.today().isoformat())
    return (
        f"Catalog size: {total} open-source projects across {cats} categories "
        f"({open_core_count} use an open-core model, marked with `*` in the license column). "
        f"Last automated sync: {updated}."
    )


def update_category_pages(data: dict[str, Any]) -> None:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in data["software"]:
        grouped.setdefault(item["category"], []).append(item)

    for cat in data["categories"]:
        detail_rel = cat.get("detail_page")
        if not detail_rel:
            continue
        detail_path = ROOT / detail_rel
        if not detail_path.exists():
            continue
        content = detail_path.read_text(encoding="utf-8")
        if "<!-- START:CATEGORY_TABLE -->" in content:
            table = render_category_table(grouped.get(cat["id"], []), include_release=True)
            content = replace_section(content, "CATEGORY_TABLE", table)
            detail_path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Update OSS catalog data and Markdown tables.")
    parser.add_argument("--fetch-github", action="store_true", help="Fetch stars, licenses, and release dates from GitHub API.")
    parser.add_argument("--check-links", action="store_true", help="Verify homepage URLs respond cleanly.")
    parser.add_argument("--render-only", action="store_true", help="Only regenerate Markdown tables from software.json.")
    args = parser.parse_args()

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    token = os.environ.get("GITHUB_TOKEN")

    if args.fetch_github and not args.render_only:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
            futures = [pool.submit(enrich_github_entry, item, token) for item in data["software"]]
            for fut in concurrent.futures.as_completed(futures):
                fut.result()
        data["metadata"]["last_updated"] = dt.date.today().isoformat()

    broken: list[tuple[str, str, int | str]] = []
    if args.check_links and not args.render_only:
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
            future_map = {pool.submit(check_url, item["url"]): item for item in data["software"]}
            for fut in concurrent.futures.as_completed(future_map):
                item = future_map[fut]
                ok, code = fut.result()
                item["link_ok"] = ok
                if not ok:
                    broken.append((item["name"], item["url"], code))

    DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if README_PATH.exists():
        readme = README_PATH.read_text(encoding="utf-8")
        readme = replace_section(readme, "STATS", render_stats(data))
        readme = replace_section(readme, "FEATURED", render_featured_table(data))
        readme = replace_section(readme, "TOC", render_toc(data))
        readme = replace_section(readme, "CATALOG", render_catalog(data))
        README_PATH.write_text(readme, encoding="utf-8")

    update_category_pages(data)

    if broken:
        print("Broken or unreachable URLs detected:", file=sys.stderr)
        for name, url, code in broken:
            print(f"  - {name}: {url} ({code})", file=sys.stderr)

    print(f"Updated {len(data['software'])} entries across {len(data['categories'])} categories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
