# Common Mistakes

Anti-patterns observed in baseline testing (without this skill). Avoid these.

| Mistake | Fix |
|---------|-----|
| Writing a custom XML parser instead of running `scripts/extract_xdm_schema.py` | Always run the extractor first — it handles all XML complexity and encoding |
| Copying raw DESC text verbatim or truncating with "…" | **Always write a fresh 3–8 word description** from the field name. Never paste raw DESC. |
| Adding `(disabled by default)` to descriptions | Do NOT — fields with `enabled: false` must be **silently skipped** from the table |
| Adding a `Schema Type` extra column to the field table | The table has exactly **4 columns**: Field, Type, Description, Origin — no extras |
| Adding `Methods:` or `Sub-containers:` extra sections under a regular entity requirement | Only the root module requirement (Step 7) may have a `**Methods:**` section |
| Using `Proposed` for Status | Use `Implemented` for existing modules. Only use `Proposed` for modules not yet in `src/` |
| Enum type using wrong name (e.g., `TestMode` instead of `TestContainerTestMode`) | Use the `req_type` value from the JSON — it is already correct |
| Setting Document Version to 1.1 or higher | Always start at `1.0` for a freshly generated document |
