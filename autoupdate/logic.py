import os

from .model import Base


def run(base: Base):
    os.system(base.com_run)

def git_update():
    os.system(f"git pull")

def git_clone(base: Base):
    os.system(f"git clone {base.git}")
