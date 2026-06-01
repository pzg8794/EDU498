#!/usr/bin/env python3
"""Validate EDU498 module structure consistency.

Checks:
- Each module uses 'Reading & Media Content' (singular).
- No module contains a plural directory named 'Readings & Media Content'.
- Required reading pipeline directories/files exist when applicable.
- If source_inventory.md declares an expected overview count, themed_overview count matches.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class ModuleReport:
    name: str
    issues: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    expected_overviews: Optional[int] = None
    actual_overviews: Optional[int] = None
    source_items: Optional[int] = None


def parse_expected_count(inventory_text: str) -> Optional[int]:
    patterns = [
        r"has\s+\*\*(\d+)\s+source items\*\*",
        r"exactly\s+\*\*(\d+)\s+readable overview files\*\*",
        r"has\s+(\d+)\s+source items",
        r"exactly\s+(\d+)\s+readable overview files",
    ]
    for pattern in patterns:
        match = re.search(pattern, inventory_text, flags=re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None


def count_source_items(source_dir: Path) -> int:
    count = 0
    for entry in source_dir.iterdir():
        if entry.name.startswith("."):
            continue
        if entry.is_file() and entry.name.lower() != "source_inventory.md":
            count += 1
    return count


def count_themed_overviews(themed_dir: Path) -> int:
    # Count only top-level markdown files as module overview artifacts.
    return sum(1 for p in themed_dir.glob("*.md") if p.is_file())


def check_module(module_dir: Path) -> ModuleReport:
    report = ModuleReport(name=module_dir.name)

    singular_dir = module_dir / "Reading & Media Content"
    plural_dir = module_dir / "Readings & Media Content"

    if plural_dir.exists():
        report.issues.append("Found deprecated directory name: 'Readings & Media Content'.")

    if not singular_dir.exists():
        report.warnings.append("Missing 'Reading & Media Content' directory.")
        return report

    source_dir = singular_dir / "source"
    themed_dir = singular_dir / "themed_overview"
    synthesis_file = singular_dir / "comprehensive_themed_overview.md"

    if not source_dir.exists():
        report.issues.append("Missing source directory under reading content.")
    if not themed_dir.exists():
        report.issues.append("Missing themed_overview directory under reading content.")
    if not synthesis_file.exists():
        report.warnings.append("Missing comprehensive_themed_overview.md.")

    if source_dir.exists():
        report.source_items = count_source_items(source_dir)
        inventory_file = source_dir / "source_inventory.md"
        if inventory_file.exists():
            expected = parse_expected_count(inventory_file.read_text(encoding="utf-8", errors="ignore"))
            report.expected_overviews = expected
        else:
            report.warnings.append("No source_inventory.md found in source directory.")

    if themed_dir.exists():
        report.actual_overviews = count_themed_overviews(themed_dir)

    if report.expected_overviews is not None and report.actual_overviews is not None:
        if report.actual_overviews != report.expected_overviews:
            report.issues.append(
                f"Overview count mismatch: expected {report.expected_overviews}, found {report.actual_overviews}."
            )

    return report


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    modules_root = repo_root / "modules"

    if not modules_root.exists():
        print("ERROR: modules directory not found.")
        return 2

    module_dirs = sorted([p for p in modules_root.iterdir() if p.is_dir() and p.name.startswith("module")])

    if not module_dirs:
        print("ERROR: No module directories found.")
        return 2

    reports: List[ModuleReport] = [check_module(m) for m in module_dirs]

    print("EDU498 Module Consistency Report")
    print("=" * 32)
    for r in reports:
        print(f"\n- {r.name}")
        if r.source_items is not None:
            print(f"  source_items: {r.source_items}")
        if r.expected_overviews is not None:
            print(f"  expected_overviews: {r.expected_overviews}")
        if r.actual_overviews is not None:
            print(f"  actual_overviews: {r.actual_overviews}")

        if r.issues:
            for issue in r.issues:
                print(f"  ISSUE: {issue}")
        if r.warnings:
            for warning in r.warnings:
                print(f"  WARN:  {warning}")
        if not r.issues and not r.warnings:
            print("  OK")

    total_issues = sum(len(r.issues) for r in reports)
    print("\nSummary")
    print("-" * 7)
    print(f"issues: {total_issues}")

    if total_issues > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
