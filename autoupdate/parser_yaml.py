import yaml
from pathlib import Path

from .model import Base
from . import config


def parse_yaml(path: str) -> Base:
    with open(path) as f:
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

def generate_yaml() -> Path:
    name = input("Name: ")
    git = input("git: ")
    time_update = input("time update: ")
    commend_run = input("commend run: ")
    base_mod = Base(
        name=name,
        git=git,
        time_update=time_update,
        command_run=commend_run,
    )
    path = Path(".", f"{name}{config.mask_yaml}")
    with open(path, "w") as f:
        f.write(yaml.safe_dump(base_mod.generate_dict()))
    return path



def generate_base_yaml(b_path="./") -> Path:
    base_mod = Base(
        name="neofetch",
        git=None,
        time_update="110",
        command_run="neofetch",
    )
    path = Path(b_path, f"neofetch{config.mask_yaml}")
    with open(path, "w") as f:
        f.write(yaml.safe_dump(base_mod.generate_dict()))
    return path
    
