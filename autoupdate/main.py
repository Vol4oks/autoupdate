import glob, time

from .parser_yaml import generate_yaml, parse_yaml
from .logic import run, send_mess_tg
from .config import standart
from .model import Base




def main():
    check_config = glob.glob(f"*{standart.mask_yaml}")
    if len(check_config) > 0:
        print(check_config)
        res = check_config[0]
    else:
        res = generate_yaml()
        print(res)
    r = parse_yaml(res)
    ceck_env = glob.glob(f"{standart.name_env}")
    if len(ceck_env) < 1:
        standart.generate_env()
    from .config import tg
    send_mess_tg(r, "START SYSTEM")

    #loop(r)

def loop(base: Base):
    time_last = time.time()
    send_mess_tg( base, "start")
    while True:
        if time.time() - time_last > int(base.time_update):
            print(run(base))
            time_last = time.time()
