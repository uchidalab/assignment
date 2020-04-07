FROM nvidia/cuda:9.0-cudnn7-runtime-ubuntu16.04
RUN apt-get update
RUN apt-get install -y python3-pip sudo git openssh-server
RUN pip3 install --upgrade pip
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y language-pack-ja-base language-pack-ja
ENV LANG=ja_JP.UTF-8
RUN apt-get install build-essential
RUN apt-get install graphviz -y
RUN pip3 install --upgrade setuptools
RUN pip3 install pydotplus
RUN pip install setuptools --upgrade
RUN pip install -q numpy==1.13.3
RUN pip install -q scipy
RUN pip install -q matplotlib
RUN pip install -q seaborn
RUN pip install -q pulp
RUN pip install -q pyomo
RUN pip install -q funcdesigner
RUN pip install -q scikit-learn
RUN pip install -q scikit-image
RUN pip install -q pandas
RUN pip install -q h5py==2.8.0rc1
RUN pip install -q requests
RUN pip install -q tensorflow-gpu==1.9.0
RUN pip install -q keras==2.1.5
RUN pip install -q gensim tqdm nltk colormath opencv-python
# ENV NB_USER your_name
# ARG HOST_UID
# ENV NB_UID ${HOST_UID}
# RUN useradd -m -G sudo -u $NB_UID $NB_USER && \
#     echo "${NB_USER}:your_password" | chpasswd && \
#     echo 'Defaults visiblepw' >> /etc/sudoers && \
#     echo 'your_name ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
# RUN touch ~/.sudo_as_admin_successful
# USER $NB_USER
