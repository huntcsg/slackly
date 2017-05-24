import json
import os
import warnings

_config = {}
_defaults = {
    'ENDPOINT_CACHE_ENABLED': False,
    'ENDPOINT_CACHE_SIZE': None,
}

_config_file_paths = [
    '~/.slackly/config.json',
]


def fill_config():
    global _config_file_paths
    if 'SLACKLY_CONFIG_FILE' in os.environ:
        _config_file_paths = [os.environ['SLACKLY_CONFIG_FILE']]

    for config_file_path in _config_file_paths:
        try:
            with open(os.path.expanduser(config_file_path), 'rb') as f:
                config_data = json.loads(f.read().decode('utf-8'))
                _config.update(config_data)
        except (OSError, IOError) as e:
            if e.errno == 2:
                # No such file or directory. That's ok
                continue
            else:
                warnings.warn("There was an error loading configuration file [ {} ]: {}".format(config_file_path, e))

        except ValueError as e:
            warnings.warn("There was an error parsing configuration file [ {} ]: {}".format(config_file_path, e))

    for key in os.environ:
        if key.startswith('SLACKLY_'):
            value = os.environ[key]

            if value == 'False':
                value = False
            elif value == 'True':
                value = True
            elif value == 'None':
                value = None
            elif value.isnumeric():
                value = int(value)

            _config[key[8:]] = value

    for key in _defaults:
        if key not in _config:
            _config[key] = _defaults[key]


fill_config()


def get_config_value(value):
    return _config.get(value, None)
