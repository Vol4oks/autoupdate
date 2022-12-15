import subprocess as sp
import os

from .model import Base
from .config import standart, tg

class Target:
    def __init__(self, base: Base) -> None:
        self.config = base
        self.error = None
        self.prog = None

    def run(self):
        self.prog = sp.Popen(self.config.com_run, shell=True)
    

def run(base: Base):
    os.system(base.com_run)

def git_update():
    return os.system(f"git pull")

def git_clone(base: Base):
    os.system(f"git clone {base.git}")

def send_mess_tg(base: Base, text: str):
    return os.system(
        f"curl -s -X POST https://api.telegram.org/bot{tg.BOT_TOKEN}/sendMessage \
            -d chat_id={tg.ADMINS} -d text='{base.name}: {text}'"
    )
