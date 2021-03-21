#!/bin/bash
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

set -e 
echo '## MLDevEnv management tool CLI interface' > help.md
echo 'ML Development Environment ships with a lower level CLI tool for automating the process of keeping conda and pip packages up-to-date.' >> help.md
echo '### Two different tools available via a single `mldevenv` cli' >> help.md
echo '```' >> help.md
mlenvtool -h >> help.md
echo '```' >> help.md
echo "### Keep versions inside a conda yaml file up-to-date " >> help.md
echo '```' >> help.md
mlenvtool conda_env_yaml_transform -h >> help.md
echo '```' >> help.md
echo "#### Create a new conda environment via" >>help.md
echo '```' >> help.md 
echo 'conda create -n my_new_env python=3.8' >>help.md
echo 'conda activate my_new_env'>>help.md
echo '```' >> help.md 
echo "#### Relax version requirements" >> help.md
echo "Apply one of the following ways of relaxing version requirements" >>help.md
echo "##### Replace strict versions with lower boundaries" >> help.md
echo '```' >> help.md
mlenvtool conda_env_yaml_transform version_eq2ge -h >> help.md
echo '```' >> help.md
echo "##### Strip version information" >> help.md
echo '```' >> help.md
mlenvtool conda_env_yaml_transform version_strip -h >> help.md
echo '```' >> help.md
echo "### Install packages from conda yaml file into the current environment" >> help.md
echo '```' >> help.md
mlenvtool conda_env_cur_update -h >> help.md
echo '```' >> help.md
echo "### Capture the package versions into the conda yaml file" >> help.md
echo '```' >> help.md
mlenvtool conda_env_yaml_transform version_capture -h >> help.md
echo '```' >> help.md
