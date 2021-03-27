#!/bin/bash
set -e
full_path=$(realpath $0)
dir_path=$(dirname $full_path)
miniconda_dir=${2:-/opt/miniconda/}
source $miniconda_dir/bin/activate ""
conda create -n $1 python=3.8 -y
conda activate $1
$dir_path/install_all.sh
