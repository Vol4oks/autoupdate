import yaml
from pathlib import Path

from .model import Base

def parse_yaml(p: str) -> Base:
    with open(p) as f:
        d = yaml.safe_load(f)
    keys = [*d.keys()]
    k = d[keys[0]]
    mod = Base(
        name=keys[0],
        git=k["git"],
        time_update=k["time_update"],
        command_run=k["command_run"]
    )
    return mod


def generate_base_yaml(b_path="./") -> Path:
    base_mod = Base(
        name="neofetch",
        git=None,
        time_update="110",
        command_run="neofetch",
    )
    path = Path(b_path, "exmple.yaml")
    with open(path, "w") as f:
        f.write(yaml.safe_dump(base_mod.generate_dict()))
    return path
    
