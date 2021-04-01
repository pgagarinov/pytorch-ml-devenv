# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).


## [unreleased.Bugfixes] - YYYY-MM-DD
### Added
 
### Changed
    ```
     conda:
	-- gensim==3.8.3
	+- gensim==4.0.0
	-- numpy==1.20.1
	+- numpy==1.20.2
	-- ipython==7.21.0
	+- ipython==7.22.0
	-- matplotlib==3.3.4
	+- matplotlib==3.4.1
	-- xeus-python==0.12.1
	+- xeus-python==0.12.2
	-- conda==4.9.2
	-- pytorch-lightning==1.2.5
	+- conda==4.10.0
	+- pytorch-lightning==1.2.6
	-- boto3==1.17.37
	+- boto3==1.17.42
	-- pytorch-lightning==1.2.5
	+- pytorch-lightning==1.2.6
	+- python-kaleido==0.2.1
     pip: 
	-  - mlflow==1.14.1
	+  - mlflow==1.15.0
	-  - wandb==0.10.23
	+  - wandb==0.10.24
  ```
### Deprecated

### Removed

### Fixed
  - ./check_if_rogue_jupyterlab_is_installed.sh now uses bash instead of zsh

## [0.2.2] - 2021-03-26
### Changed
 - Updated some of the packages
     - conda dependencies
	     ```
		-- nltk==3.4.4
		+- nltk==3.5
		-- pytorch::pytorch==1.8.0
		-- pytorch::torchvision==0.9.0
		-- pytorch::torchtext==0.9.0
		-- pytorch::torchaudio==0.8.0
		+- pytorch::pytorch==1.8.1
		+- pytorch::torchvision==0.9.1
		+- pytorch::torchtext==0.9.1
		+- pytorch::torchaudio==0.8.1
		-- xeus-python==0.12.0
		-- catboost==0.24.4
		+- xeus-python==0.12.1
		+- catboost==0.25
		-- lightgbm==3.1.1
		+- lightgbm==3.2.0
		-- notebook==6.2.0
		+- notebook==6.3.0
		-- jupyterlab-lsp==3.4.1
		+- jupyterlab-lsp==3.5.0
		-- ipympl==0.6.3
		+- ipympl==0.7.0
		-- pytorch-lightning==1.2.4
		+- pytorch-lightning==1.2.5
		-- boto3==1.17.33
		+- boto3==1.17.37
		-- pytorch-lightning==1.2.4
		+- pytorch-lightning==1.2.5
		```
		
      - pip dependencies:
		```
		-  - jupytext==1.11.0
		+  - jupytext==1.11.1
		-  - wandb==0.10.22
		+  - wandb==0.10.23
		```
### Fixed
  - ./check_if_rogue_jupyterlab_is_installed.sh now uses bash instead of zsh

## [0.2.1] - 2021-03-22

### Added
 - MLEnvTool:
   - usage scenarios described in README.md
   - version_capture transformation for capturing versions of the conda and pip packages inside   the specified conda environment into the conda environment yaml file; this transform complements version_eq2ge and version_strip transforms to make it possible to keep both conda and pip packages up-to-date with minimial efforts
   - greatly improved command line help
 - New conda packages: 
    - jupyterlab_execute_time==2.0.2
    - plotly==4.14.3
    - pytorch-lightning==1.2.4
 - New jupyterlab extensions:
    - jupyterlab-plotly@v4.14.3
 - `generate_help.sh` shell script to capture the cli help of MLEnvTool (helps to keep README.md up-to-date)
 
### Changed
 - Major update of all the package versions including PyTorch (to v1.8) and torchvision (to v.0.9)
 - Major refactoring of MLEnvTool internals to improve source code readibility and maintainability
 - pyyaml moved from pip to conda section in the conda env yaml file

### Deprecated

### Removed

### Fixed
 - MLDevEnv: pip package versions are now generated correctly
 - `#!/bin/bash` is moved to the first line in all bash script


