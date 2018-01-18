import json
from pathlib import Path


PATH = '{}/.whoisrc'.format(str(Path.home()))


def _load_configurations():
    try:
        with open(PATH, 'r') as f:
            configurations = f.read()
            configurations = json.loads(configurations)
    except FileNotFoundError as e:
        configurations = {'default': None, 'tokens': []}
        _update_configurations(configurations)
    return configurations


def _update_configurations(configurations):
    with open(PATH, 'w') as f:
        f.write(json.dumps(configurations))


def add_token(token):
    configurations = _load_configurations()
    if token not in configurations['tokens']:
        configurations['tokens'].append(token)
    if not configurations['default']:
        set_default_token(token)
        return
    _update_configurations(configurations)


def set_default_token(token=None, position=None):
    configurations = _load_configurations()
    if not position:
        try:
            position = configurations['tokens'].index(token)
        except ValueError:
            configurations['tokens'].append(token)
            position = -1
    configurations['default'] = configurations['tokens'][position]
    return _update_configurations(configurations)

def get_tokens():
    configurations = _load_configurations()
    return configurations['tokens']


def get_default_token():
    configurations = _load_configurations()
    return configurations['default']
