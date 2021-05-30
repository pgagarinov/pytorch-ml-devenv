# PyTorch ML Development Environment
is a set of modern ML-oriented conda and pip packages with versions carefully chosen to make sure a seamless and conflict-free integration. 

## Prerequisites Features
1. Linux operating system. The testing and development is done in Manjaro Linux. Windows and MacOS are not supported and there are no such plans. This limitation will be less critical once the docker container becomes available.
2. conda 4.9 or later. The recommended conda distribution is Miniconda. The environment is based on conda, conda channels (mostly `conda-forge`) are preferred to PyPI where possible. The recommended way of installing Miniconda on Manjaro Linux is [install_miniconda.sh](https://github.com/Alliedium/awesome-linux-config/blob/master/manjaro/basic/install_miniconda.sh) script.

## Features
1. The only IDE provided by the environment is JupyterLab. 
2. We try and usually we are on the bleeding edge in terms of package versions used. The closes analog to PyTorch HyperLight MLDevEnv project is (ml-workspace)[https://github.com/ml-tooling/ml-workspace] project. What makes MLDevEnv different is that packages included into MLDevEnv are usually MUCH more recent comparing to the packages in ml-workspace. This becomes possible because
3. The environment is built around PyTorch, XGBoost, Catboost, Scikit-Learn and a few other frameworks with non-conflicting dependencies.
4. TensorFlow is not included as it usually have dependency on specific versions of CUDA that conflicts with CUDA version that PyTorch depends on.

## Planned features
1. Docker containers 

## Features we do not want
1. Support for TensorFlow, MXNet, Caffe


## Installation
1. Create the conda environment and install the dependencies via runing the following commands without `sudo`:
```bash
source /opt/miniconda/bin/activate
conda env create -n ml-devenv python=3.8
conda activate ml-devenv
./install_all.sh
```
2. Optionally run `./run_all.sh ml-devenv` to launch the JupyterLab server, TensorBoard server and MLFlow server.

## MLDevEnv management tool CLI interface
ML Development Environment ships with a lower level CLI tool for automating the process of keeping conda and pip packages up-to-date.
### Two different tools available via a single `mldevenv` cli
```
usage: mlenvtool [-h] {conda_env_yaml_transform,conda_env_cur_update}

MLDevEnv management tool

positional arguments:
  {conda_env_yaml_transform,conda_env_cur_update}
                        Choose one of possible strategies: conda_env_cur_update: Update current conda environment by installing 
                                                additional packages,
                        conda_env_yaml_transform: Transforms conda YAML environment file using one 
                                                    of the predefined algorithms.

optional arguments:
  -h, --help            show this help message and exit
```
### Keep versions inside a conda yaml file up-to-date 
```
usage: mlenvtool conda_env_yaml_transform [-h] transform

Transforms conda YAML environment file using one of the predefined algorithms.

positional arguments:
  transform   Name of the conda yaml file transform to apply. The following transforms are supported:
              
              version_capture: This mode scans the specified yaml file and fixes the 
                                 package versions to those from the specified conda 
                                 environment. The typical usecase for this mode is to run 
                                 version_eq2ge, then update the environment and then, 
                                 finally, run version_capture to update the environment 
                                 definition yaml file with the new fixed versions of the 
                                 packages,
              version_eq2ge: This mode scans the specified yaml file and and replaces the 
                               exact versions specified via `==` with lower limit on the 
                               version number specified via `>=` version specification for 
                               each of the packages,
              version_strip: This mode scans the specified yaml file and strips version 
                               information for each of the packages keepting the reset of 
                               the package definition intact; `pytorch::torchvision==0.9` 
                               would be replaced with `pytorch::torchvision`

optional arguments:
  -h, --help  show this help message and exit
```
#### Create a new conda environment via
```
conda create -n my_new_env python=3.8
conda activate my_new_env
```
#### Relax version requirements
Apply one of the following ways of relaxing version requirements
##### Replace strict versions with lower boundaries
```
usage: mlenvtool conda_env_yaml_transform version_eq2ge [-h]
                                                        [--in_yaml_file IN_YAML_FILE]
                                                        [--out_yaml_file OUT_YAML_FILE]
                                                        [--except_package_list PACKAGE_NAME [PACKAGE_NAME ...]]
                                                        [-y]

This mode scans the specified yaml file and and replaces the exact versions specified via `==` with lower limit on the version number specified via `>=` version specification for each of the packages

optional arguments:
  -h, --help            show this help message and exit
  --in_yaml_file IN_YAML_FILE
                        Input conda environment yaml file path
  --out_yaml_file OUT_YAML_FILE
                        Output conda environment yaml file path
  --except_package_list PACKAGE_NAME [PACKAGE_NAME ...]
                        Packages to exclude from transformation
  -y                    Suppresses prompt for confirmation
```
##### Strip version information
```
usage: mlenvtool conda_env_yaml_transform version_strip [-h]
                                                        [--in_yaml_file IN_YAML_FILE]
                                                        [--out_yaml_file OUT_YAML_FILE]
                                                        [--except_package_list PACKAGE_NAME [PACKAGE_NAME ...]]
                                                        [-y]

This mode scans the specified yaml file and strips version information for each of the packages keepting the reset of the package definition intact; `pytorch::torchvision==0.9` would be replaced with `pytorch::torchvision`

optional arguments:
  -h, --help            show this help message and exit
  --in_yaml_file IN_YAML_FILE
                        Input conda environment yaml file path
  --out_yaml_file OUT_YAML_FILE
                        Output conda environment yaml file path
  --except_package_list PACKAGE_NAME [PACKAGE_NAME ...]
                        Packages to exclude from transformation
  -y                    Suppresses prompt for confirmation
```
### Install packages from conda yaml file into the current environment
```
usage: mlenvtool conda_env_cur_update [-h] [-y] [--update_mode] [-d]

Update current conda environment by installing additional packages

optional arguments:
  -h, --help      show this help message and exit
  -y              Suppresses prompt for confirmation
  --update_mode   What to update
                  The following modes are supported:
                  
                  all: filter_requirements: False,
                         install_modules: True,
                         install_requirements: True,
                         jlab_install_extensions: True,
                         module_names: [],
                  allbutjupyterext: filter_requirements: False,
                                      install_modules: True,
                                      install_requirements: True,
                                      jlab_install_extensions: False,
                                      module_names: [],
                  jupyterext: filter_requirements: False,
                                install_modules: False,
                                install_requirements: False,
                                jlab_install_extensions: True,
                                module_names: [],
                  packages: filter_requirements: False,
                              install_modules: False,
                              install_requirements: True,
                              jlab_install_extensions: False,
                              module_names: [],
                  products: filter_requirements: False,
                              install_modules: True,
                              install_requirements: False,
                              jlab_install_extensions: False,
                              module_names: []
  -d, --debug     update with debug logs
```
### Capture the package versions into the conda yaml file
```
usage: mlenvtool conda_env_yaml_transform version_capture [-h]
                                                          [--in_yaml_file IN_YAML_FILE]
                                                          [--out_yaml_file OUT_YAML_FILE]
                                                          [--except_package_list PACKAGE_NAME [PACKAGE_NAME ...]]
                                                          [-y]
                                                          [--conda_env_path CONDA_ENV_PATH]

This mode scans the specified yaml file and fixes the package versions to those from the specified conda environment. The typical usecase for this mode is to run version_eq2ge, then update the environment and then, finally, run version_capture to update the environment definition yaml file with the new fixed versions of the packages

optional arguments:
  -h, --help            show this help message and exit
  --in_yaml_file IN_YAML_FILE
                        Input conda environment yaml file path
  --out_yaml_file OUT_YAML_FILE
                        Output conda environment yaml file path
  --except_package_list PACKAGE_NAME [PACKAGE_NAME ...]
                        Packages to exclude from transformation
  -y                    Suppresses prompt for confirmation
  --conda_env_path CONDA_ENV_PATH
                        Full path to conda environment
```
