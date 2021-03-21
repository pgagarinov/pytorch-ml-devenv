#!/bin/bash
set -e 
echo '## MLDevEnv management tool CLI interface' > help.md
echo 'ML Development Environment ships with a lower level CLI tool for automating the process of keeping Conda and pip packages up-to-date.' >> help.md
echo '### Two different tools available via a single `mldevenv` cli' >> help.md
echo '```' >> help.md
mlenvtool -h >> help.md
echo '```' >> help.md
echo "### Keep versions inside a Conda yaml file up-to-date " >> help.md
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
echo "### Install packages from Conda yaml file into the current environment" >> help.md
echo '```' >> help.md
mlenvtool conda_env_cur_update -h >> help.md
echo '```' >> help.md
echo "### Capture the package versions into the Conda yaml file" >> help.md
echo '```' >> help.md
mlenvtool conda_env_yaml_transform version_capture -h >> help.md
echo '```' >> help.md
