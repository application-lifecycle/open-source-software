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
import html
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
DOCS_DIR = ROOT / "docs"
SITE_URL = "https://application-lifecycle.github.io/open-source-software/"
GSC_META_TAG = '<meta name="google-site-verification" content="HqgfQrEQATXaycciOAu8GzuJP8BSRHtaR1JrgBtnApU" />'
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


def render_docs_site(data: dict[str, Any]) -> None:
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    updated = data["metadata"].get("last_updated", dt.date.today().isoformat())
    total = len(data["software"])
    cat_count = len(data["categories"])

    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in data["software"]:
        grouped.setdefault(item["category"], []).append(item)

    toc_links = []
    sections_html = []
    for cat in data["categories"]:
        cid = html.escape(cat["id"])
        cname = html.escape(cat["name"])
        csum = html.escape(cat["summary"])
        items = grouped.get(cat["id"], [])
        toc_links.append(f'<a href="#{cid}">{cname} ({len(items)})</a>')

        rows = []
        for item in items:
            name = html.escape(item["name"])
            url = html.escape(item["url"])
            alt = html.escape(item["alternative_to"])
            plats = html.escape(", ".join(item["platforms"]))
            lic = item["license"]
            if item.get("open_core") and "open-core" not in lic.lower():
                lic = f"{lic} *"
            lic_esc = html.escape(lic)
            stars = html.escape(format_stars(item.get("stars")))
            status = html.escape(item.get("status", "Active"))
            mig = html.escape(item["migration"])
            best = html.escape(item["best_for"])
            search_blob = html.escape(
                f"{item['name']} {item['alternative_to']} {item['license']} {item['best_for']} {cat['name']}".lower()
            )
            rows.append(
                f'<tr data-search="{search_blob}">'
                f'<td><a href="{url}" target="_blank" rel="noopener">{name}</a></td>'
                f'<td>{alt}</td>'
                f'<td>{plats}</td>'
                f'<td>{lic_esc}</td>'
                f'<td>{stars}</td>'
                f'<td>{status}</td>'
                f'<td>{mig}</td>'
                f'<td>{best}</td>'
                f'</tr>'
            )

        sections_html.append(
            f'<section id="{cid}" class="cat-section">\n'
            f'  <h2>{cname}</h2>\n'
            f'  <p class="cat-summary">{csum}</p>\n'
            f'  <div class="table-wrap"><table>\n'
            f'    <thead><tr><th>Software</th><th>Alternative to</th><th>Platform</th>'
            f'<th>License</th><th>Stars</th><th>Activity</th><th>Migration</th><th>Best for</th></tr></thead>\n'
            f'    <tbody>\n      ' + "\n      ".join(rows) + "\n    </tbody>\n"
            f'  </table></div>\n'
            f'</section>'
        )

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Best Open Source Software (OSS) - Curated Directory</title>
  <meta name="description" content="A curated list of the best open-source software by category, platform, license and use case." />
  <link rel="canonical" href="{SITE_URL}" />
  {GSC_META_TAG}
  <style>
    :root {{ --bg: #ffffff; --fg: #1f2328; --muted: #59636e; --border: #d1d9e0; --accent: #0969da; --surface: #f6f8fa; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; color: var(--fg); background: var(--bg); line-height: 1.55; }}
    .wrap {{ max-width: 1180px; margin: 0 auto; padding: 32px 20px 64px; }}
    header {{ border-bottom: 1px solid var(--border); padding-bottom: 20px; margin-bottom: 24px; }}
    h1 {{ margin: 0 0 10px; font-size: 2rem; }}
    h2 {{ margin: 36px 0 6px; font-size: 1.35rem; }}
    p {{ margin: 0 0 12px; }}
    .meta {{ color: var(--muted); font-size: 0.92rem; }}
    .actions {{ margin-top: 14px; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
    .btn {{ display: inline-block; padding: 7px 14px; border: 1px solid var(--border); border-radius: 6px; text-decoration: none; color: var(--fg); background: var(--surface); font-size: 0.9rem; }}
    .btn:hover {{ border-color: var(--accent); color: var(--accent); }}
    #filter {{ width: 100%; max-width: 420px; padding: 8px 12px; border: 1px solid var(--border); border-radius: 6px; font-size: 0.95rem; }}
    .toc {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 18px 0 28px; }}
    .toc a {{ padding: 4px 10px; border: 1px solid var(--border); border-radius: 999px; font-size: 0.85rem; color: var(--fg); text-decoration: none; background: var(--surface); }}
    .toc a:hover {{ border-color: var(--accent); color: var(--accent); }}
    .cat-summary {{ color: var(--muted); font-size: 0.95rem; margin-bottom: 12px; }}
    .table-wrap {{ overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
    th, td {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--border); vertical-align: top; }}
    th {{ background: var(--surface); font-weight: 600; white-space: nowrap; }}
    a {{ color: var(--accent); }}
    footer {{ margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--border); color: var(--muted); font-size: 0.9rem; }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>Best Open Source Software (OSS)</h1>
      <p>A curated directory of the best open-source software by category, platform, license, commercial alternative, and migration difficulty. Projects marked with <code>*</code> use an open-core model.</p>
      <p class="meta">Catalog size: {total} open-source projects across {cat_count} categories. Last automated sync: {html.escape(updated)}.</p>
      <div class="actions">
        <input id="filter" type="search" placeholder="Filter by software, alternative (e.g. Photoshop, Salesforce), or license..." aria-label="Filter software directory" />
        <a class="btn" href="https://github.com/application-lifecycle/open-source-software">View on GitHub</a>
        <a class="btn" href="https://github.com/application-lifecycle/open-source-software/blob/main/migration-guides/salesforce-to-twenty.md">Salesforce to Twenty Guide</a>
        <a class="btn" href="https://github.com/application-lifecycle/open-source-software/blob/main/migration-guides/photoshop-to-gimp.md">Photoshop to GIMP Guide</a>
      </div>
    </header>
    <nav class="toc" aria-label="Categories">
      {" ".join(toc_links)}
    </nav>
    <main>
      {"".join(sections_html)}
    </main>
    <footer>
      <p>Maintained in <a href="https://github.com/application-lifecycle/open-source-software">application-lifecycle/open-source-software</a> under the MIT License. Star counts, release dates, and license metadata sync weekly from GitHub.</p>
    </footer>
  </div>
  <script>
    const input = document.getElementById("filter");
    const sections = Array.from(document.querySelectorAll(".cat-section"));
    input.addEventListener("input", () => {{
      const q = input.value.trim().toLowerCase();
      sections.forEach((sec) => {{
        let visible = 0;
        sec.querySelectorAll("tbody tr").forEach((tr) => {{
          const match = !q || tr.dataset.search.includes(q);
          tr.style.display = match ? "" : "none";
          if (match) visible++;
        }});
        sec.style.display = visible > 0 ? "" : "none";
      }});
    }});
  </script>
</body>
</html>
"""
    (DOCS_DIR / "index.html").write_text(index_html, encoding="utf-8")

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{SITE_URL}</loc>
    <lastmod>{html.escape(updated)}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    (DOCS_DIR / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")

    robots_txt = f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}sitemap.xml\n"
    (DOCS_DIR / "robots.txt").write_text(robots_txt, encoding="utf-8")
    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")


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
    render_docs_site(data)

    if broken:
        print("Broken or unreachable URLs detected:", file=sys.stderr)
        for name, url, code in broken:
            print(f"  - {name}: {url} ({code})", file=sys.stderr)

    print(f"Updated {len(data['software'])} entries across {len(data['categories'])} categories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
