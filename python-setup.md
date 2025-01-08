# Python setup

## Install Pyenv for current uer
Pyenv help manage multiple version of Python

Ref:
- https://github.com/pyenv/pyenv?tab=readme-ov-file#installation

## Use Pyenv to install Python

View available Python versions

    pyenv install -l

Install

    pyenv install 3
    pyenv global 3

Confirm python

    which python
    python --version

Confirm all installed python versions in Pyenv

    pyenv versions

# pipx - Install and Run Python Applications in Isolated Environments
Install

    sudo apt update
    sudo apt install pipx
    pipx ensurepath
    sudo pipx ensurepath --global # optional to allow pipx actions with --global argument

Ref:
- https://github.com/pypa/pipx

## Poetry
Python packaging and dependency management made easy

### Install
    pipx install poetry

Ref:
- https://python-poetry.org/docs/#ci-recommendations

### Poetry usage
Check current Poetry configuration

    poetry config --list

`~/.config/pypoetry/config.toml` will be automatically created when you first config something using `poetry config`

Tell poetry to create virtual environments in the current project directory (`.venv`)

    poetry config virtualenvs.in-project true

Create new project

    poetry new poetry-demo

Initialising a pre-existing project

    poetry init

The poetry env activate command prints the activate command of the virtual environment to the console. You can run the output command manually or feed it to the eval command of your shell to activate the environment. This way you won’t leave the current shell.

    eval $(poetry env activate)
    
Verify virtual environment activated

    which python 
    # print python path pointing from '.\venv\'

To deactivate the virtual environment without leaving the shell use `deactivate`.

Displays information about the current environment

    poetry env info

If you only want to know the path to the virtual environment, you can pass the --path option to env info:

    poetry env info --path

Listing the environments associated with the project

    poetry env list
    poetry env list --full-path

Add and install dependencies

    poetry add <package-name>

Install dependencies from existing `pyproject.toml`

    poetry intall

 Searches for packages on remote repositories.

    poetry search <package-name>

The cache list command lists Poetry’s available caches.

    poetry cache list

To clear the whole cache of packages from the PyPI repository, run:

    poetry cache clear PyPI --all

To clear all caches

    poetry cache clear --all .

- https://python-poetry.org/docs/basic-usage/
- https://python-poetry.org/docs/managing-environments/

### Jupyter Notebook with Poetry

Install Jupyter Notebook as Poetry dev dependency

    poetry add -D notebook

Run notebook in Virtual environment

    poetry run jupyter notebook
    # OR
    eval $(poetry env activate)
    jupyter notebook

## Pip-autoremove

When using `pip` to uninstall package, it only removes the specified package, it doesn't uninstall the dependencies packages. 

To install package and it's dependencies, we use `pip3-autoremove`

    pip install pip3-autoremove
    pip3-autoremovev <package-name>