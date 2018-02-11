#!/bin/sh

git clone https://github.com/riywo/anyenv ~/.anyenv
anyenv install pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.anyenv/envs/pyenv/plugins/pyenv-virtualenv
exec $SHELL -l
pyenv install miniconda3-latest
