import os


def get_current_conda_env_path():
    return os.environ["CONDA_PREFIX"]


def get_current_conda_env_name():
    return os.environ["CONDA_DEFAULT_ENV"]
