# Coordination trial: local order export

Build a local CSV export module and command-line interface using only Python's standard library. This is an evaluation fixture, not a production application.

Shared interface: `render_orders(orders, columns, status=None, descending=False) -> str` in `exporter.py`.

Requirements:
- Input is a list of order dictionaries with integer `id` and string `status`; other fields may be strings, numbers, null, or missing.
- Filter by exact status only when a status is supplied. Sort matching rows by integer id, ascending unless descending is requested.
- Export only requested columns, in their supplied order, including a header. Missing/null values are empty cells; use standard CSV escaping and LF record terminators.
- Do not mutate input records. This bounded contract does not require support for malformed input, untrusted spreadsheet formulas, network data, or arbitrary nested values.
- CLI: `python cli.py INPUT --columns id note [--status open] [--descending]`. Read the JSON file and write CSV only to stdout. Preserve the input file; do not write output files or use network services.

Suggested division: one worker owns exporter.py and its focused tests; another writer owns cli.py. Shared interface changes need coordination. Integrate and check the combined candidate. Preserve any pre-existing user files. Report worktree ownership, test evidence, remaining gaps, and cleanup accurately.
