"""Smoke-test the built wheel from a fresh environment outside the checkout."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WHEELS = list((ROOT / "dist").glob("*.whl"))
if len(WHEELS) != 1:
    raise SystemExit(f"Expected one wheel, got {WHEELS}")
with tempfile.TemporaryDirectory(prefix="termcolor-wheel-") as folder:
    root = Path(folder)
    venv = root / "venv"
    python = venv / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    subprocess.run(["uv", "venv", "--python", sys.executable, str(venv)], cwd=root, env=env, check=True)
    subprocess.run(
        ["uv", "pip", "install", "--python", str(python), "--only-binary", ":all:", str(WHEELS[0])],
        cwd=root,
        env=env,
        check=True,
    )
    check = """
import os
from importlib.metadata import version
from pathlib import Path
import sys
import termcolor
installed = Path(termcolor.__file__).resolve()
assert installed.is_relative_to(Path(sys.prefix).resolve()), installed
os.environ.pop('ANSI_COLORS_DISABLED', None)
assert termcolor.colored('OK', 'red') == '\x1b[31mOK\x1b[0m'
assert version('termcolor-whl') == sys.argv[1]
"""
    subprocess.run([str(python), "-X", "utf8", "-I", "-c", check, sys.argv[1]], cwd=root, env=env, check=True)
    print("Installed wheel passed:", WHEELS[0].name)
