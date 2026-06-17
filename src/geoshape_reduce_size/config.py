import yaml
from pathlib import Path

# config.yaml lives at the project root, two levels up from src/geoshape_reduce_size/
_CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config.yaml"

def _load() -> dict:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_path(key: str) -> str:
    val = _load()["paths"][key]
    p = Path(val)
    if not p.is_absolute():
        p = (_CONFIG_PATH.parent / p).resolve()
    return str(p)

def get_value(key: str):
    """Read a top-level config value (e.g. simplify_tolerance)."""
    return _load()[key]

