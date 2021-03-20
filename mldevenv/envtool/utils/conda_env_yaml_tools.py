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

import yaml
from conda.models.match_spec import MatchSpec
from yaml import CLoader
from conda.models.version import VersionSpec
from functools import partial


def load_environment(environment_file):
    with open(environment_file, "r") as f:
        environment = yaml.load(f, Loader=CLoader)
    return environment


def dump_environment(environment, environment_file):
    with open(environment_file, "w") as f:
        yaml.dump(environment, f)


def proc_tree(dep_list, func):
    spec_list = []
    for dep in dep_list:
        if isinstance(dep, dict):
            dep_dict = dep
            spec = {}
            for key, val_dep_list in dep_dict.items():
                spec[key] = proc_tree(val_dep_list, func)
        else:
            spec = func(dep)
        spec_list.append(spec)
    return spec_list


def match_spec_fixed_parse(inp_str):
    ind_name_right = min([ind for ind, c in enumerate(inp_str) if c in '~=!<>'])
    ind_name_left = inp_str.find('::')
    if ind_name_left<0:
        ind_name_left =0
    else:
        ind_name_left = ind_name_left+2

    orig_name = inp_str[ind_name_left: ind_name_right]
    match_spec = MatchSpec(inp_str, name = orig_name)
    return match_spec


def parse_dependencies(dep_list):
    spec_list = proc_tree(dep_list, match_spec_fixed_parse)
    return spec_list


def match_spec2str(match_spec):
    res_str = match_spec.spec
    if 'channel' in match_spec._match_components:
        channel = match_spec._match_components['channel']
        res_str = f'{channel}::{res_str}'
    return res_str


def serialize_dependencies(spec_list):
    dep_list = proc_tree(spec_list, match_spec2str)
    return dep_list


def version_eq2ge(spec, except_name_list=None):
    if (except_name_list is None) or (spec.name not in except_name_list):
        # noinspection PyProtectedMember
        kwargs = {
            key: value
            for key, value in spec._match_components.items()
            if key == "channel"
        }
        spec = MatchSpec(
            version=VersionSpec(">=" + str(spec.version.matcher_vo)),
            name=spec.name,
            **kwargs
        )
    return spec


def version_strip(spec, except_name_list=None):
    if (except_name_list is None) or (spec.name not in except_name_list):
        # noinspection PyProtectedMember
        kwargs = {
            key: value
            for key, value in spec._match_components.items()
            if key == "channel"
        }
        spec = MatchSpec(name=spec.name, **kwargs)
    return spec


def proc_env_dependencies(environment, func):
    spec_list = parse_dependencies(environment["dependencies"])
    spec_list = proc_tree(spec_list, func)
    environment["dependencies"] = serialize_dependencies(spec_list)
    return environment


def env_depversions_strip(environment, except_name_list=None):
    func = partial(version_strip, except_name_list=except_name_list)
    return proc_env_dependencies(environment, func)


def env_depversions_eq2ge(environment, except_name_list=None):
    func = partial(version_eq2ge, except_name_list=except_name_list)
    return proc_env_dependencies(environment, func)


def conda_yaml_versions_strip(in_yaml, out_yaml, **kwargs):
    environment = load_environment(in_yaml)
    environment = env_depversions_strip(environment, **kwargs)
    dump_environment(environment, out_yaml)


def conda_yaml_versions_eq2ge(in_yaml, out_yaml, **kwargs):
    environment = load_environment(in_yaml)
    environment = env_depversions_eq2ge(environment, **kwargs)
    dump_environment(environment, out_yaml)
