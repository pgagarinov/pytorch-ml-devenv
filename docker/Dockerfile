FROM nvidia/cuda:11.2.2-base 
ARG CONDA_ENV_NAME=ml-devenv-0
ARG USER_NAME=ml-devenv-user
RUN useradd $USER_NAME -m
RUN apt update
RUN apt install git gcc g++ p7zip-rar wget sudo -y 
RUN echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USER_NAME
ENV TERM xterm
RUN cd ~ && git clone https://github.com/Alliedium/awesome-linux-config.git 
RUN cd ~ && git clone https://github.com/pgagarinov/pytorch-ml-devenv.git
RUN ~/awesome-linux-config/manjaro/basic/user/config_jupyter.sh
RUN ~/awesome-linux-config/manjaro/basic/install_miniconda.sh
SHELL ["/bin/bash", "-c"]
RUN ~/pytorch-ml-devenv/create_install_all.sh $CONDA_ENV_NAME

