# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [unreleased.Bugfixes] - YYYY-MM-DD

### Added
 - MLEnvTool:
   - usage scenarios described in README.md
   - version_capture transformation for capturing versions of the conda and pip packages inside   the specified conda environment into the conda environment yaml file; this transform complements version_eq2ge and version_strip transforms to make it possible to keep both conda and pip packages up-to-date with minimial efforts
   - greatly improved command line help
 - New conda packages: 
    - jupyterlab_execute_time==2.0.2
    - plotly==4.14.3
 - New jupyterlab extensions:
    - jupyterlab-plotly@v4.14.3
 - `generate_help.sh` shell script to capture the cli help of MLEnvTool (helps to keep README.md up-to-date)
 
### Changed
 - Major update of all the package versions including PyTorch (to v1.8) and torchvision (to v.0.9)
 - Major refactoring of MLEnvTool internals to improve source code readibility and maintainability

### Deprecated

### Removed

### Fixed
 - MLDevEnv: pip package versions are now generated correctly


