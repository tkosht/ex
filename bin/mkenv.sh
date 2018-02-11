#!/bin/sh

ENV_NAME="labex"
if [ "$1" != "" ]; then
    ENV_NAME="$1"
fi

pyenv virtualenv miniconda3-latest $ENV_NAME
mkdir -p $ENV_NAME
cd $ENV_NAME
pyenv local $ENV_NAME
