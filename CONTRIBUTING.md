# Contributing to Best Open Source Software (OSS)

Contributions that keep this catalog accurate and useful are welcome. Because the tables in `README.md` and `categories/*.md` are generated from `data/software.json`, edit the JSON file directly and regenerate the Markdown tables.

## Inclusion criteria

A project belongs in this catalog when it meets all four rules:

1. The core edition uses an OSI-approved open-source license (such as MIT, Apache-2.0, GPL, LGPL, AGPL, MPL-2.0, BSD, or OSL-3.0). Source-available licenses like BSL, SSPL, or Elastic License 2.0 are excluded.
2. The repository has recent commits or releases within the last 12 months.
3. The entry names the commercial software it replaces, supported platforms, and a realistic migration difficulty (`Low`, `Medium`, or `High`).
4. If the vendor sells paid enterprise modules or uses a dual-license model, `"open_core"` is set to `true` and `"license"` names the exact open-source edition (for example, `AGPL-3.0 (Community)`).

## How to submit a change

1. Fork the repository and create a branch.
2. Edit `data/software.json` to add or update an entry.
3. Run the generator locally to refresh the Markdown tables:

```bash
python3 scripts/update-directory.py --render-only
```

4. Check `git diff` to verify the table formatting and link targets.
5. Open a pull request explaining why the software belongs in the category or what changed in its license or maintenance status.

## Reporting broken links or license changes

If a listed project switches away from an open-source license, gets archived, or changes its homepage URL, open an issue with a link to the official announcement or license file.
