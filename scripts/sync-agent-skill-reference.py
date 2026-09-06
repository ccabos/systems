#!/usr/bin/env python3
"""Regenerate projects/agent-skill/reference/ from knowledge/.

The agent skill is uploaded to claude.ai as a self-contained bundle, so it
cannot read knowledge/ at runtime: SKILL.md points at reference/ throughout.
The mirror is therefore unavoidable — but it is *generated*, never edited.
knowledge/ stays the canonical home, as CONTRIBUTING.md requires.

    python3 scripts/sync-agent-skill-reference.py            # write the mirror
    python3 scripts/sync-agent-skill-reference.py --check    # verify only

--check exits non-zero when a mirrored file is missing, differs from its
source, or is present in the mirror without being listed below. CI runs it
on every push and pull request.

To add a file to the bundle, add its knowledge/-relative path to MANIFEST
and re-run. To drop one, remove it here and delete the mirrored copy.
"""

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SOURCE = REPO / "knowledge"
MIRROR = REPO / "projects" / "agent-skill" / "reference"

# Files kept in the bundle, as paths relative to knowledge/.
MANIFEST = [
    # Techniques the skill reads on every run.
    "se-techniques/control-structures/dangerous-patterns.md",
    "se-techniques/control-structures/diagnostic-questions.md",
    "se-techniques/goals-requirements-hierarchy/five-level-hierarchy.md",
    "se-techniques/justification-rungs/dangerous-mismatches.md",
    "se-techniques/justification-rungs/rungs.md",
    "se-techniques/stpa/four-steps.md",
    "se-techniques/stpa/unsafe-control-actions.md",
    # Development frameworks: cross-framework material and each decomposition.
    "system-catalogues/dev-frameworks/cross-framework/hybrids.md",
    "system-catalogues/dev-frameworks/cross-framework/merging-principles.md",
    "system-catalogues/dev-frameworks/cross-framework/platform.md",
    "system-catalogues/dev-frameworks/cross-framework/reuse-analysis.md",
    "system-catalogues/dev-frameworks/cross-framework/variation-points.md",
    "system-catalogues/dev-frameworks/design-thinking/se-decomposition.md",
    "system-catalogues/dev-frameworks/devops/se-decomposition.md",
    "system-catalogues/dev-frameworks/kanban/se-decomposition.md",
    "system-catalogues/dev-frameworks/prince2/se-decomposition.md",
    "system-catalogues/dev-frameworks/safe/se-decomposition.md",
    "system-catalogues/dev-frameworks/scrum/se-decomposition.md",
    "system-catalogues/dev-frameworks/v-model/se-decomposition.md",
    "system-catalogues/dev-frameworks/waterfall/se-decomposition.md",
    # Social systems: cross-system material, each decomposition, one worked example.
    "system-catalogues/social-systems/cross-system/justification-rungs-by-system.md",
    "system-catalogues/social-systems/cross-system/platform.md",
    "system-catalogues/social-systems/cross-system/remedies-case-studies.md",
    "system-catalogues/social-systems/cross-system/variation-points.md",
    "system-catalogues/social-systems/corporation/se-decomposition.md",
    "system-catalogues/social-systems/democracy/se-decomposition.md",
    "system-catalogues/social-systems/family/se-decomposition.md",
    "system-catalogues/social-systems/kingdom/se-decomposition.md",
    "system-catalogues/social-systems/military/se-decomposition.md",
    "system-catalogues/social-systems/one-party-state/se-decomposition.md",
    "system-catalogues/social-systems/religion/applied-se-analysis.md",
    "system-catalogues/social-systems/religion/se-decomposition.md",
    "system-catalogues/social-systems/theocracy/se-decomposition.md",
    "system-catalogues/social-systems/university/se-decomposition.md",
    "system-catalogues/social-systems/verein/se-decomposition.md",
]

# Hand-written files that live in the mirror but come from nowhere.
NOT_MIRRORED = {"README.md", "memo-template.md", "report-template.md"}


def mirrored_files():
    """Every .md under the mirrored subtrees, relative to MIRROR."""
    found = set()
    for sub in ("se-techniques", "system-catalogues"):
        root = MIRROR / sub
        if root.is_dir():
            found |= {p.relative_to(MIRROR).as_posix() for p in root.rglob("*.md")}
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="report drift and exit non-zero instead of writing")
    args = ap.parse_args()

    missing_source, stale, copied = [], [], []

    for rel in MANIFEST:
        src, dst = SOURCE / rel, MIRROR / rel
        if not src.is_file():
            missing_source.append(rel)
            continue
        if dst.is_file() and filecmp.cmp(src, dst, shallow=False):
            continue
        if args.check:
            stale.append(rel + ("" if dst.exists() else "  (fehlt im Bündel)"))
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
            copied.append(rel)

    orphans = sorted(f for f in mirrored_files()
                     if f not in set(MANIFEST) and Path(f).name not in NOT_MIRRORED)

    if missing_source:
        print("Im Manifest gelistet, aber nicht in knowledge/ vorhanden:")
        for r in missing_source:
            print("  ", r)
    if orphans:
        print("Im Bündel, aber nicht im Manifest (verwaist — von Hand löschen "
              "oder ins Manifest aufnehmen):")
        for r in orphans:
            print("  ", r)

    if args.check:
        if stale:
            print("Weicht von knowledge/ ab:")
            for r in stale:
                print("  ", r)
        if stale or orphans or missing_source:
            print("\nreference/ ist nicht synchron. Beheben mit:")
            print("    python3 scripts/sync-agent-skill-reference.py")
            return 1
        print("reference/ ist synchron mit knowledge/ (%d Dateien)." % len(MANIFEST))
        return 0

    if missing_source:
        return 1
    print("%d Dateien aktualisiert, %d bereits aktuell."
          % (len(copied), len(MANIFEST) - len(copied) - len(missing_source)))
    for r in copied:
        print("  ", r)
    return 0


if __name__ == "__main__":
    sys.exit(main())
