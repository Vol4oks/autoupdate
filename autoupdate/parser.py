import yaml

from .model import Base

def parse(p: str) -> Base:
    with open(p) as f:
        d = yaml.safe_load(f)
    keys = [*d.keys()]
    print(keys)
    d = d[keys[0]]
    mod = Base(
        name=d["name"],
        git=d["git"],
        time_update=d["time_update"],
    )

    return mod