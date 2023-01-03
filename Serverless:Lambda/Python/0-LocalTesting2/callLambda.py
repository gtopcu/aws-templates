from importlib import import_module
import os
import json

from lambda_configs import function_config_map


def execute_lambda(lambda_conf):
    lambda_env = lambda_conf.get('environment', {})
    print(lambda_env)
    lambda_path = lambda_conf['path']
    lambda_module_path = f"{lambda_path.replace('/', '.')}.index"

    _add_env_variables(lambda_env)

    lambda_function = import_module(lambda_module_path)

    event = _read_lambda_event_file(f"../spikyai_cdk_core/{lambda_path}/local/event.json")

    try:
        lambda_result = lambda_function.handler(event, {})
    except Exception:
        raise Exception
    finally:
        _clear_env_variables(lambda_env)

    return lambda_result


def _add_env_variables(env: dict):
    for key, value in env.items():
        os.environ[key] = value


def _clear_env_variables(env: dict):
    for key in env.keys():
        del os.environ[key]


def _read_lambda_event_file(event_path: str):
    with open(event_path) as fp:
        return json.load(fp)


if __name__ == "__main__":
    function_name = "PlatformCore"
    lambda_config = function_config_map[function_name]
    result = execute_lambda(lambda_config)
    print(result)