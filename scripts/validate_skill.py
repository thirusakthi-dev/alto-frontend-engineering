from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRS = {".git", ".venv", ".tools", "__pycache__", ".pytest_cache"}
VENV_SCRIPTS = ROOT / ".venv" / ("Scripts" if sys.platform == "win32" else "bin")


def find_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in EXCLUDED_DIRS for part in path.parts)
    )


def run_check(name: str, command: list[str]) -> bool:
    print(f"\n{'=' * 60}")
    print(name)
    print("=" * 60)

    result = subprocess.run(command, cwd=ROOT, check=False)

    if result.returncode == 0:
        print(f"\nPASS: {name}")
        return True

    print(f"\nFAIL: {name} (exit code {result.returncode})")
    return False


def skip_check(name: str, reason: str) -> None:
    print(f"\nSKIP: {name} — {reason}")


def find_executable(name: str) -> str | None:
    executable = f"{name}.exe" if sys.platform == "win32" else name
    local_path = VENV_SCRIPTS / executable

    if local_path.is_file():
        return str(local_path)

    return shutil.which(name)


def find_lychee() -> str | None:
    configured_path = os.environ.get("LYCHEE_PATH")

    if configured_path:
        path = Path(configured_path)

        if path.is_file():
            return str(path)

        print(f"\nWARNING: LYCHEE_PATH does not exist: {configured_path}")

    executable = find_executable("lychee")

    if executable:
        return executable

    if sys.platform == "win32":
        packages_dir = (
            Path(os.environ.get("LOCALAPPDATA", ""))
            / "Microsoft"
            / "WinGet"
            / "Packages"
        )

        for package in packages_dir.glob("lycheeverse.lychee*"):
            for match in package.glob("**/lychee.exe"):
                return str(match)

    return None


def main() -> int:
    results: list[tuple[str, bool]] = []
    markdown_files = find_markdown_files()
    uv = shutil.which("uv")

    if not markdown_files:
        print("No Markdown files found.")
        return 1

    print(f"Repository: {ROOT}")
    print(f"Markdown files found: {len(markdown_files)}")

    format_markdown_files = [
        path for path in markdown_files if path != ROOT / "SKILL.md"
    ]

    # Agent Skill validation
    skills_ref = find_executable("skills-ref")

    if skills_ref:
        results.append(
            (
                "Agent Skill validation",
                run_check(
                    "Agent Skill validation",
                    [skills_ref, "validate", str(ROOT)],
                ),
            )
        )
    else:
        skip_check(
            "Agent Skill validation",
            "skills-ref executable not found",
        )

    # Python tooling through uv
    if uv:
        results.append(
            (
                "Markdown formatting",
                run_check(
                    "Markdown formatting",
                    [
                        uv,
                        "run",
                        "--no-sync",
                        "mdformat",
                        "--check",
                        *map(str, format_markdown_files),
                    ],
                ),
            )
        )

        scripts_dir = ROOT / "scripts"

        if scripts_dir.is_dir():
            results.append(
                (
                    "Python linting",
                    run_check(
                        "Python linting",
                        [
                            uv,
                            "run",
                            "--no-sync",
                            "ruff",
                            "check",
                            str(scripts_dir),
                        ],
                    ),
                )
            )

            results.append(
                (
                    "Python formatting",
                    run_check(
                        "Python formatting",
                        [
                            uv,
                            "run",
                            "--no-sync",
                            "ruff",
                            "format",
                            "--check",
                            str(scripts_dir),
                        ],
                    ),
                )
            )

        test_files = [
            path
            for path in ROOT.rglob("test_*.py")
            if not any(part in EXCLUDED_DIRS for part in path.parts)
        ]

        if test_files:
            results.append(
                (
                    "Python tests",
                    run_check(
                        "Python tests",
                        [uv, "run", "--no-sync", "pytest"],
                    ),
                )
            )
        else:
            skip_check(
                "Python tests",
                "No Python test files found yet",
            )

    else:
        skip_check(
            "Python tooling",
            "uv is not installed or not available in PATH",
        )

    # Markdown link checking
    lychee = find_lychee()

    if lychee:
        results.append(
            (
                "Markdown link checking",
                run_check(
                    "Markdown link checking",
                    [
                        lychee,
                        "--no-progress",
                        "--accept",
                        "200..=299, 403",
                        *map(str, markdown_files),
                    ],
                ),
            )
        )
    else:
        skip_check(
            "Markdown link checking",
            "Lychee executable not found",
        )

    # Summary
    print(f"\n{'=' * 60}")
    print("VALIDATION SUMMARY")
    print("=" * 60)

    for name, passed in results:
        print(f"{'PASS' if passed else 'FAIL'}: {name}")

    failures = sum(not passed for _, passed in results)

    print(f"\nPassed: {len(results) - failures}")
    print(f"Failed: {failures}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
