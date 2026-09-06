# reference/ — generated, do not edit

Everything under `se-techniques/` and `system-catalogues/` in this folder
is a **copy** of a file in the repository's `knowledge/` tree. The copies
exist because the skill is uploaded to claude.ai as a self-contained
bundle: at runtime there is no `knowledge/` to read, and `SKILL.md`
points at `reference/` throughout.

**Editing a file here loses the edit.** Change the file in `knowledge/`,
then regenerate:

```bash
python3 scripts/sync-agent-skill-reference.py
```

CI runs `--check` on every push and pull request and fails if the two
trees have drifted, so the copies cannot quietly diverge again.

`memo-template.md` and `report-template.md` are the exception: they
belong to the skill, have no counterpart in `knowledge/`, and are edited
here.

Which files are bundled is decided by the `MANIFEST` list in the sync
script. To add one, add its `knowledge/`-relative path there and re-run.
