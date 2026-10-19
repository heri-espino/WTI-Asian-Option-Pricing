"""Fail a public release if filenames or text suggest licensed raw data/secrets."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED = {"data", "results", "raw", "private", "vendor", "archive", "literature", "secrets"}
EXT = {".csv", ".dbn", ".parquet", ".xlsx", ".zip", ".jsonl", ".sqlite", ".arrow", ".feather", ".pkl"}
SECRETS = re.compile(r"(?i)(?:api[_-]?key|token|password|secret)\s*[:=]\s*['\"][A-Za-z0-9_.-]{15,}['\"]")
HEADER = re.compile(r"(?i)Time,Open,High,Low,Latest,Change")

def validate() -> None:
    bad=[]
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        rel=path.relative_to(ROOT)
        if path.is_symlink() or path.suffix.lower() in EXT or any(p.lower() in BANNED for p in rel.parts):
            bad.append(str(rel))
        if path.suffix.lower() in {".py", ".md", ".yml", ".toml", ".cff", ".json"}:
            content=path.read_text(encoding="utf-8",errors="replace")
            if SECRETS.search(content) or (HEADER.search(content) and path.name!="check_public_release.py"):
                bad.append(str(rel)+" (suspected secret or vendor rows)")
    if bad:
        raise SystemExit("Public release blocked:\n"+"\n".join(sorted(set(bad))))
    print("Public repository content check passed (path/format and common-secret heuristics)")

if __name__ == "__main__":
    validate()
