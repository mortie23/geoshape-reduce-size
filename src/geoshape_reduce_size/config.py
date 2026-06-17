import yaml
from pathlib import Path

# config.yaml lives at the project root, two levels up from src/geoshape_reduce_size/
_CONFIG_PATH = Path(__file__).resolve().parent.parent.parent / "config.yaml"

def get_path(key: str) -> str:
    with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    val = config["paths"][key]
    # Resolve relative paths against the project root
    p = Path(val)
    if not p.is_absolute():
        p = (_CONFIG_PATH.parent / p).resolve()
    return str(p)

