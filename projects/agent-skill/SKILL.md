# SKILL manifest — placeholder

<!--
    This file is a placeholder for the agent skill manifest. It will
    be written after the knowledge base in ../../knowledge/ has
    stabilised enough that the skill can cite specific files with
    confidence. Until then, the README in this folder describes the
    intended shape of the skill and the hard rules it must follow.
-->

**Status:** not yet implemented.

When implemented, this file will contain:

- The skill's `name`, `description`, and trigger conditions.
- The system prompt instructing the model to walk a user through
  the **eight-step** procedure described in `README.md` (the
  seventh of the original steps was split when the
  justificatory-rung tagging was added between control-structure
  sketch and STPA pass).
- Explicit references to `../../knowledge/se-techniques/` files for
  every technique step, including the rung extension at
  `../../knowledge/se-techniques/justification-rungs/`.
- A check after step 5 (rung tagging) that determines whether the
  social-systems extension was needed: if the system is engineering
  or technical and all loops operate at rung 3–4 throughout, step 5
  is documented as N/A rather than executed.
- Output format rules that produce artefacts suitable for filing
  under `../problems/<problem-name>/`.
