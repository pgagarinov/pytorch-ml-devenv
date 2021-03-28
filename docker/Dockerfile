FROM archlinux

ARG CONDA_ENV_NAME=ml-devenv-0
ARG USER_NAME=ml-devenv-user
RUN useradd $USER_NAME -m
RUN pacman -Syy
RUN pacman -S git gcc unrar wget sudo --noconfirm --needed
RUN echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USER_NAME
ENV TERM xterm
RUN cd ~ && git clone https://github.com/Alliedium/awesome-linux-config.git 
RUN cd ~ && git clone https://github.com/pgagarinov/pytorch-ml-devenv.git
RUN ~/awesome-linux-config/manjaro/basic/user/config_jupyter.sh
RUN ~/awesome-linux-config/manjaro/basic/install_miniconda.sh
SHELL ["/bin/bash", "-c"]
RUN ~/pytorch-ml-devenv/create_install_all.sh $CONDA_ENV_NAME \ 
    && ~/.conda/envs/${CONDA_ENV_NAME}/bin/conda clean -ay \
    && rm -rf ~/.cache

# https://github.com/NVIDIA/nvidia-container-runtime#environment-variables-oci-spec
ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

