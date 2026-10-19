#!/usr/bin/env python3
"""Build a fresh, deliberately allowlisted public research repo from the private tree.

Usage (PowerShell):
  python prepare_public_repository.py --source C:\\path\\to\\Bayesian-Uncertainty-in-WTI-APOs --dest C:\\path\\to\\WTI-Asian-Option-Pricing

This creates a directory, not a Git remote, DOI, or Git history. Do NOT fork or
mirror the original repo: it contains licensed market-data histories.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

NAME = "WTI-Asian-Option-Pricing"
EXPERIMENTS = (
    "experiments/",  # all experiment source .py files, never data/results
)
TESTS = {
    "test_asian_pricing.py",
    "test_bayesian_gbm.py",
    "test_bayesian_student_t.py",
    "test_gaussian_sigma_quadrature.py",
    "test_american_futures_option.py",
    "test_synthetic_validation.py",
    "test_wti_apo_pricing.py",
    "test_curran_futures_pricing.py",
    "test_accelerated_pricing.py",
}
FORBIDDEN_SUFFIXES = {
    ".csv", ".dbn", ".parquet", ".xlsx", ".xls", ".jsonl", ".sqlite",
    ".db", ".h5", ".hdf5", ".arrow", ".feather", ".pkl", ".pickle",
    ".ipynb", ".gz", ".zip", ".7z", ".rar", ".pdf", ".jpg", ".jpeg",
}
BLOCKED_PATH_PARTS = {
    "data", "results", "raw", "vendor", "literature", "archive",
    "notebooks", ".git", ".venv", "secrets", "credentials", "private",
    "market-data", "market_data", "node_modules", "__pycache__",
}
SECRET_PATTERNS = (
    re.compile(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_.-]{15,}['\"]"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)
PRICE_HEADER = re.compile(r"(?i)Time,Open,High,Low,Latest,Change")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(2**20), b""):
            h.update(block)
    return h.hexdigest()


def safe_copy(src: Path, dst: Path, source_root: Path, destination_root: Path) -> None:
    if src.is_symlink() or not src.is_file():
        raise ValueError(f"Not a regular source file: {src}")
    src.relative_to(source_root)
    if dst.suffix.lower() in FORBIDDEN_SUFFIXES:
        raise ValueError(f"Forbidden public file extension: {dst}")
    if any(x.lower() in BLOCKED_PATH_PARTS for x in dst.relative_to(destination_root).parts):
        raise ValueError(f"Forbidden destination path component: {dst}")
    if src.stat().st_size > 3_000_000:
        raise ValueError(f"Unexpectedly large source file: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def _original_commit(root: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True,
            stderr=subprocess.DEVNULL, timeout=5,
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return "not-recorded"


def build(source: Path, destination: Path, kit: Path) -> None:
    source = source.resolve()
    destination = destination.resolve()
    if source == destination or source in destination.parents or destination in source.parents:
        raise ValueError("Destination must be outside the private source tree")
    required = source / "bayesian_asian_options" / "src" / "bayesian_asian_options"
    if not (required / "__init__.py").is_file() or not (source / "pyproject.toml").is_file():
        raise ValueError("Source is not the expected private WTI Asian-option repository")
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Destination must be absent or empty; never overwrite a repository")
    destination.mkdir(parents=True, exist_ok=True)

    # Same import name; simpler modern source layout, no git ancestry copied.
    modules = sorted(required.glob("*.py"))
    if len(modules) < 10:
        raise ValueError("Unexpectedly few library modules; inspect source")
    for file in modules:
        safe_copy(file, destination / "src" / "bayesian_asian_options" / file.name, source, destination)

    experiments = sorted((source / "experiments").glob("*.py"))
    if len(experiments) < 20:
        raise ValueError("Unexpected experiment inventory; inspect source")
    for file in experiments:
        safe_copy(file, destination / "experiments" / file.name, source, destination)
    for filename in sorted(TESTS):
        src = source / "tests" / filename
        if not src.exists():
            raise FileNotFoundError(f"Selected scientific test missing: {src}")
        safe_copy(src, destination / "tests" / filename, source, destination)

    # Only a synthetic-mechanism figure, not raw or empirical contract-level data.
    mechanism = source / "figures" / "publication" / "fig01_mechanism_map.png"
    if mechanism.is_file():
        # PNG is not treated as raw price data and is explicitly curated.
        if mechanism.is_symlink() or mechanism.stat().st_size > 20_000_000:
            raise ValueError("Unexpected synthetic figure file")
        target = destination / "figures" / "synthetic_posterior_integration.png"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(mechanism, target)

    # Include the concise, self-contained S1--S4 supplement as a *candidate*
    # for author/editor review; discard all legacy appended archives.
    supplement = source / "paper" / "supplement" / "online_supplement.md"
    if supplement.is_file():
        text = supplement.read_text(encoding="utf-8")
        text = text.split("\n## Archive A.", 1)[0].rstrip() + "\n"
        if not all(f"## S{i}." in text for i in range(1, 5)):
            raise ValueError("Supplement is missing an expected S1--S4 heading")
        out = destination / "supplement" / "robustness_and_numerical_checks.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")

    for item in kit.iterdir():
        if item.name == "prepare_public_repository.py":
            continue
        if item.is_file() and (item.name == ".gitignore" or item.suffix in {".md", ".toml", ".yml", ".yaml", ".cff", ".txt"}):
            out = destination / item.name
            out.write_bytes(item.read_bytes())
    # Include selected nested curated docs and CI definitions (never hidden data).
    for root_name in ("docs", ".github", "scripts"):
        root = kit / root_name
        if root.exists():
            for file in root.rglob("*"):
                if file.is_file():
                    out = destination / file.relative_to(kit)
                    out.parent.mkdir(parents=True, exist_ok=True)
                    out.write_bytes(file.read_bytes())

    manifest = {
        "origin_repository": "heri-espino/Bayesian-Uncertainty-in-WTI-APOs",
        "origin_commit": _original_commit(source),
        "source_mode": "explicit curated export, no original git history",
        "raw_market_data_exported": False,
        "files": {},
    }
    for file in sorted(x for x in destination.rglob("*") if x.is_file()):
        manifest["files"][file.relative_to(destination).as_posix()] = sha256(file)
    (destination / "SOURCE_PROVENANCE.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    scan_release(destination)
    print(f"Prepared {len(manifest['files'])} files at {destination}")
    print("REVIEW REQUIRED: no release, public push, or Zenodo DOI has been created.")
    print("Review license, files, tests, supplement and citation metadata first.")


def scan_release(directory: Path) -> None:
    errors: list[str] = []
    for file in directory.rglob("*"):
        if not file.is_file():
            continue
        relative = file.relative_to(directory)
        if file.is_symlink():
            errors.append(f"symlink: {relative}")
        if any(part.lower() in BLOCKED_PATH_PARTS for part in relative.parts):
            errors.append(f"restricted path: {relative}")
        if file.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"restricted extension: {relative}")
        if file.name.endswith(".env") or file.name in {".env", "id_rsa"}:
            errors.append(f"credential filename: {relative}")
        if file.stat().st_size > 20_000_000:
            errors.append(f"unexpectedly large file: {relative}")
        if file.suffix.lower() in {".py", ".md", ".txt", ".toml", ".yml", ".yaml", ".json", ".cff"}:
            text = file.read_text(encoding="utf-8", errors="replace")
            if PRICE_HEADER.search(text) and relative.as_posix() != "scripts/check_public_release.py":
                errors.append(f"Barchart price CSV signature: {relative}")
            if any(pattern.search(text) for pattern in SECRET_PATTERNS):
                errors.append(f"possible embedded secret: {relative}")
    if errors:
        raise ValueError("Public release blocked:\n- " + "\n- ".join(errors))
    print("Public release scanner: no blocked data files, raw formats or obvious secrets")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--dest", type=Path, required=True)
    args = parser.parse_args()
    build(args.source, args.dest, Path(__file__).resolve().parent)


if __name__ == "__main__":
    main()
