from autoupdate.parser_yaml import parse_yaml, generate_base_yaml
from autoupdate.logic import run

def start():
    path = generate_base_yaml()
    res = parse_yaml(path)
    print(res)
    run(res)

