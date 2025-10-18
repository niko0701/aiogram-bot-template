from pathlib import Path
import yaml


def load_texts() -> dict:
    yaml_path = Path.cwd() / "texts.yml"

    if not yaml_path.exists():
        raise FileNotFoundError(f"texts.yml not found in {Path.cwd()}")

    with open(yaml_path, "r", encoding="utf-8") as f:
        texts_dict = yaml.safe_load(f)

    return texts_dict
