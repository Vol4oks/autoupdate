import glob, time

from .parser_yaml import generate_yaml, parse_yaml
from .logic import run
from . import config
from .model import Base

def main():
    check_config = glob.glob(f"*{config.mask_yaml}")
    if len(check_config) > 0:
        print(check_config)
        res = check_config[0]

    else:
        res = generate_yaml()
        print(res)
    r = parse_yaml(res)

    loop(r)

def loop(base: Base):
    time_last = time.time()
    while True:
        if time.time() - time_last > int(base.time_update):
            run(base)
            time_last = time.time()
