from datetime import datetime
from pathlib import Path
import subprocess

ALLOWED_APPS = {
    "notepad": ["notepad.exe"],
    "calculator": ["calc.exe"],
}

def current_time() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")

def list_files(path: str = ".") -> list[str]:
    return [p.name for p in Path(path).expanduser().resolve().iterdir()]

def open_allowed_app(name: str) -> str:
    key = name.lower().strip()
    if key not in ALLOWED_APPS:
        raise ValueError("Aplicación no permitida.")
    subprocess.Popen(ALLOWED_APPS[key])
    return f"{key} abierto."
