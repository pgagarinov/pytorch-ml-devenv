# Copyright Peter Gagarinov.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from pathlib import Path
import sys
from mldevenv.envtool.utils.conda_env_deployment_tool import (
    update_current_conda_env,
)
import mldevenv.envtool.utils.conda_env_yaml_tools as yts
from mldevenv.envtool.utils.common import get_current_conda_env_path
from pprint import pprint, pformat
from mldevenv.envtool.utils.conda_env_deployment_tool import ENV_UPDATE_MODE2CMD_DICT

MAIN_CMD_NAME = "mlenvtool"

TRANSFORM_DESCRIPTION_DICT = {
    "version_strip": "This mode scans the specified yaml file and strips version information for each of the packages "
    "keepting the reset of the package definition intact; `pytorch::torchvision==0.9` would be replaced with `pytorch::torchvision`",
    "version_eq2ge": "This mode scans the specified yaml file and and replaces the exact versions specified via `==` with lower limit on the version number "
    "specified via `>=` version specification for each of the packages",
    "version_capture": "This mode scans the specified yaml file and fixes the package versions to those from the specified conda environment. "
    "The typical usecase for this mode is to run version_eq2ge, then update the environment and then, finally, "
    "run version_capture to update the environment definition yaml file with the new fixed versions of the packages",
}


TRANSFORM_CMD2FUNC_MAP_DICT = {
    "version_strip": yts.conda_yaml_version_strip,
    "version_eq2ge": yts.conda_yaml_version_eq2ge,
    "version_capture": yts.conda_yaml_version_capture,
}

CURRENT_PATH: Path = Path(__file__).absolute()
MLDEVENV_CONDA_REQA_FILE_NAME = "mldevenv_conda_requirements.yml"
MLDEVENV_CONDA_REQ_FILE_ABS_PATH = (
        CURRENT_PATH.parents[2] / MLDEVENV_CONDA_REQA_FILE_NAME
)

STRATEGY_DESCRIPTION_DICT =\
    {"conda_env_yaml_transform":
         "Transforms Conda YAML environment file using one of the predefined algorithms.",
     "conda_env_cur_update":
         "Update current conda environment by installing additional packages"
    }

def check_if_yaml_file_to_path(file_name):
    path = Path(file_name)
    assert path.suffix == ".yml", f"file {file_name} doesn't have YAML file expension"
    return path.absolute()


def check_if_abs_path2dir(dir_name):
    path = Path(dir_name)
    assert path.is_absolute(), f"Path {path} is not absolute"
    assert path.is_dir(), f"Folder {path} doesn't exist"
    return path


def get_prog_name(ind_last_arg2print=1) -> str:
    arg_str = " ".join(sys.argv[1 : ind_last_arg2print + 1])
    return f"{MAIN_CMD_NAME} {arg_str}"


def pformat4help(obj,indent=0):
    help_str = pformat(obj, compact=False, indent=indent). \
        replace('"', '').replace("'", "").replace("{", "").replace("}", "")
    return help_str


def add_cli_args(arg_parser: argparse.ArgumentParser, arg_group_list):

    assert set(arg_group_list).issubset(
        ["conda_env_yaml_transform", "conda_env_yaml_transform_cmd", "conda_env_path", "yes_no_confirm",
            "conda_env_update_mode"]
    )

    if "conda_env_path" in arg_group_list:
        arg_parser.add_argument(
            "--conda_env_path",
            help="Full path to conda environment",
            type=check_if_abs_path2dir,
            required=False,
            default=get_current_conda_env_path(),
        )

    if "conda_env_yaml_transform_cmd" in arg_group_list:
        help_str = pformat4help(TRANSFORM_DESCRIPTION_DICT)

        arg_parser.add_argument(
            "conda_env_yaml_transform_cmd",
            metavar="transform",
            help=f"Name of the conda yaml file transform to apply. The following transforms are supported:\n\n{help_str}",
            choices=TRANSFORM_DESCRIPTION_DICT.keys(),
            type=str,
        )

    if "conda_env_yaml_transform" in arg_group_list:
        arg_parser.add_argument(
            "--in_yaml_file",
            help="Input conda environment yaml file path",
            type=check_if_yaml_file_to_path,
            required=False,
            default=MLDEVENV_CONDA_REQA_FILE_NAME
        )
        arg_parser.add_argument(
            "--out_yaml_file",
            help="Output conda environment yaml file path",
            type=check_if_yaml_file_to_path,
            required=False,
            default=None,
        )
        arg_parser.add_argument(
            "--except_package_list",
            nargs="+",
            metavar="PACKAGE_NAME",
            help="Packages to exclude from transformation",
            required=False,
            default=None,
        )

    if "yes_no_confirm" in arg_group_list:
        arg_parser.add_argument(
            "-y",
            help="Suppresses prompt for confirmation",
            action='store_true',
            required=False,
            default=False
        )

    if "conda_env_update_mode" in arg_group_list:
        help_str = pformat4help(ENV_UPDATE_MODE2CMD_DICT)
        arg_parser.add_argument(
            "--update_mode",
            help="What to update\n"
                 f"The following modes are supported:\n\n{help_str}",
            choices=ENV_UPDATE_MODE2CMD_DICT.keys(),
            default="all",
            metavar="",
            required=False
        )

        arg_parser.add_argument(
            "-d", "--debug", action="store_true", help="update with debug logs"
        )


def confirm(arg_dict, op_name):
    is_confirmed = arg_dict.pop('y')

    msg = f"Operation '{op_name}' is going to be applied with the following parameters:\n"
    print(f"{msg}")
    param_str = pformat4help(arg_dict, indent=3)
    print(f"{param_str}\n")
    if not is_confirmed:
        confirm_answer = input(":: Proceed with applying the transformation? [Y/n]")
        if confirm_answer.lower() != 'y':
            sys.exit(1)

def conda_env_yaml_transform_cli():

    arg_parser = argparse.ArgumentParser(
        prog=get_prog_name(1),
        description=STRATEGY_DESCRIPTION_DICT["conda_env_yaml_transform"],
        formatter_class=argparse.RawTextHelpFormatter,
    )

    add_cli_args(arg_parser, ["conda_env_yaml_transform_cmd"])
    args = arg_parser.parse_args(args=sys.argv[2:3])
    conda_env_yaml_transform_cmd = args.conda_env_yaml_transform_cmd

    arg_parser = argparse.ArgumentParser(
        prog=get_prog_name(2),
        description=TRANSFORM_DESCRIPTION_DICT[conda_env_yaml_transform_cmd],
        formatter_class=argparse.RawTextHelpFormatter,
    )

    add_cli_args(arg_parser, ["conda_env_yaml_transform", "yes_no_confirm"])

    if conda_env_yaml_transform_cmd == "version_capture":
        add_cli_args(arg_parser, ["conda_env_path"])

    args = arg_parser.parse_args(args=sys.argv[3:])

    transform_func = TRANSFORM_CMD2FUNC_MAP_DICT[conda_env_yaml_transform_cmd]

    if args.out_yaml_file is None:
        args.out_yaml_file = args.in_yaml_file

    arg_dict = dict(args._get_kwargs())
    confirm(arg_dict, conda_env_yaml_transform_cmd)

    transform_func(**arg_dict)


def conda_env_cur_update_cli():

    arg_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog=get_prog_name(),
        formatter_class=argparse.RawTextHelpFormatter,
        description=STRATEGY_DESCRIPTION_DICT["conda_env_cur_update"],
    )

    add_cli_args(arg_parser, ["conda_env_update_mode", "yes_no_confirm"])

    args = arg_parser.parse_args(args=sys.argv[2:])

    arg_dict = dict(args._get_kwargs())
    update_mode = args.update_mode
    confirm(arg_dict, update_mode)

    update_current_conda_env(MLDEVENV_CONDA_REQ_FILE_ABS_PATH, **arg_dict)


def cli_strategy():
    argument_parser = argparse.ArgumentParser(
        prog=MAIN_CMD_NAME,
        formatter_class=argparse.RawTextHelpFormatter,
        description="MLDevEnv management tool",
    )
    help_str = pformat4help(STRATEGY_DESCRIPTION_DICT)
    argument_parser.add_argument(
        "strategy",
        help=f"Choose one of possible strategies: {help_str}",
        choices=STRATEGY_DESCRIPTION_DICT.keys()
    )
    args = argument_parser.parse_args(args=sys.argv[1:2])
    strategy_name_cli_func_map: dict = {
        "conda_env_yaml_transform": conda_env_yaml_transform_cli,
        "conda_env_cur_update": conda_env_cur_update_cli,
    }

    cli_func = strategy_name_cli_func_map[args.strategy]
    cli_func()


if __name__ == "__main__":
    cli_strategy()
