"""Verify release metadata and dependency entry points without licensed data."""
from pathlib import Path
from importlib.metadata import metadata
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def test_mit_license_in_package_metadata():
    raw = (ROOT / "pyproject.toml").read_bytes()
    package = tomllib.loads(raw.decode("utf-8"))["project"]
    assert package["license"] == "MIT"
    assert package["license-files"] == ["LICENSE"]
    assert "Copyright (c) 2026 Heriberto Espino-Montelongo" in (
        ROOT / "LICENSE"
    ).read_text(encoding="utf-8")
    dist = metadata("wti-asian-option-pricing")
    assert dist["License-Expression"] == "MIT"


def test_requirement_files_use_project_extras():
    assert (ROOT / "requirements.txt").read_text().strip().endswith("-e .")
    assert (ROOT / "requirements-dev.txt").read_text().strip().endswith(
        "-e .[dev]"
    )
    assert (ROOT / "requirements-market.txt").read_text().strip().endswith(
        "-e .[dev,market]"
    )
    for filename in ("environment.yml", "environment-market.yml"):
        text = (ROOT / filename).read_text(encoding="utf-8")
        assert "python=3.11" in text
        assert "conda-forge" in text
        assert "-e .[" in text
