# FROM ubuntu:22.04

# ENV PYTHON_VERSION 3.9.17
# ENV NODE_MAJOR 16
# ENV DEBIAN_FRONTEND=noninteractive
# #Set of all dependencies needed for pyenv to work on Ubuntu
# RUN apt-get update \ 
#     && apt-get install -y --no-install-recommends make build-essential libssl-dev libpq-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget ca-certificates curl gnupg llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8 git postgresql-client telnet unzip zlib1g-dev

# RUN curl https://cli-assets.heroku.com/install.sh | sh
# RUN mkdir -p /etc/apt/keyrings && \
#     curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
#     echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list  && \
#     apt-get update && apt-get install nodejs -y

# ARG USERNAME=codeany
# RUN useradd -ms /bin/bash $USERNAME
# USER $USERNAME
# WORKDIR /home/$USERNAME

# # Set-up necessary Env vars for PyEnv
# ENV PYENV_ROOT /home/$USERNAME/.pyenv
# ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# # Install pyenv
# RUN set -ex \
#     && curl https://pyenv.run | bash \
#     && pyenv update \
#     && pyenv install $PYTHON_VERSION \
#     && pyenv global $PYTHON_VERSION \
#     && pyenv rehash \
#     && python3 -m pip install --no-cache-dir --upgrade pip \
#     && python3 -m pip install --no-cache-dir --upgrade setuptools wheel virtualenv pipenv pylint rope flake8  mypy autopep8 pep8 pylama pydocstyle bandit notebook twine

# ENV PATH=$PATH:"/home/codeany/.local/bin"

# RUN echo 'alias python=python3' >> ~/.bashrc && \
#     echo 'export PIP_USER=yes' >> ~/.bashrc && \
#     echo 'alias pip=pip3' >> ~/.bashrc && \
#     echo 'alias psql="psql mydb"' >>  ~/.bashrc

# COPY ./build-assets/heroku_config.sh /home/$USERNAME/.theia/heroku_config.sh
# RUN echo 'alias heroku_config=". $HOME/.theia/heroku_config.sh"' >> ~/.bashrc

# COPY ./build-assets/make_url.py /home/$USERNAME/.theia/make_url.py
# RUN echo 'alias make_url="python3 $HOME/.theia/make_url.py "' >> ~/.bashrc

# COPY ./build-assets/http_server.py /home/$USERNAME/.theia/http_server.py
# RUN echo 'alias http_server="python3 $HOME/.theia/http_server.py "' >> ~/.bashrc


# USER root
# RUN chown -R $USERNAME:$USERNAME /home/$USERNAME/.theia

# CMD ["tail", "-f", "/dev/null"]

# # Allows proxy to work for react/drf on cloud ide's
# ENV DANGEROUSLY_DISABLE_HOST_CHECK=true

FROM gitpod/workspace-full

USER root

# Install MongoDB
# Import the public key used by the MongoDB package management system
RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - \
    # Create a list file for MongoDB
    && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list \
    # Update the package list
    && apt-get update \
    # Install MongoDB packages
    && apt-get install -y mongodb-org \
    # Cleanup
    && rm -rf /var/lib/apt/lists/* && apt-get clean \
    # Create the MongoDB data directory
    && mkdir -p /workspace/mongodb/data \
    # Adjust ownership and permissions
    && chown -R gitpod:gitpod /workspace/mongodb

# Switch back to the gitpod user for the rest of the installations
USER gitpod

# Customize the environment
ENV PYTHON_VERSION=3.9.17 \
    NODE_VERSION=16 \
    PYENV_ROOT=/home/gitpod/.pyenv \
    PATH=$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH:/workspace/mongodb/bin \
    MONGO_PATH=/workspace/mongodb \
    MONGO_DATA_PATH=${MONGO_PATH}/data

# Install specific Python version using pyenv
RUN curl https://pyenv.run | bash \
    && $PYENV_ROOT/bin/pyenv install $PYTHON_VERSION \
    && $PYENV_ROOT/bin/pyenv global $PYTHON_VERSION \
    && $PYENV_ROOT/bin/pyenv rehash

# Use nvm (installed in the gitpod/workspace-full image) to install and use a specific Node.js version
RUN bash -i -c 'nvm install $NODE_VERSION && nvm use $NODE_VERSION && nvm alias default $NODE_VERSION'

# Additional Python packages
RUN python3 -m pip install --upgrade pip setuptools wheel virtualenv pipenv pylint rope flake8 mypy autopep8 pep8 pylama pydocstyle bandit notebook twine

# Copy any custom scripts or configuration files
COPY --chown=gitpod:gitpod ./build-assets/heroku_config.sh /home/gitpod/.heroku_config.sh
COPY --chown=gitpod:gitpod ./build-assets/make_url.py /home/gitpod/.make_url.py
COPY --chown=gitpod:gitpod ./build-assets/http_server.py /home/gitpod/.http_server.py

# Setup custom aliases and environment variables
RUN echo 'export PIP_USER=yes' >> ~/.bashrc \
    && echo 'alias python=python3' >> ~/.bashrc \
    && echo 'alias pip=pip3' >> ~/.bashrc \
    && echo 'alias psql="psql mydb"' >> ~/.bashrc \
    && echo 'alias heroku_config=". $HOME/.heroku_config.sh"' >> ~/.bashrc \
    && echo 'alias make_url="python3 $HOME/.make_url.py"' >> ~/.bashrc \
    && echo 'alias http_server="python3 $HOME
