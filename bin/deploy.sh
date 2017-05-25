#!/usr/bin/env bash

set -e

# This assumes you have a master slackly directory
# that contains slackly and slackly_utils
# and has a virtual environment called "venv"
source ../venv/bin/activate

# Get the current (working) version
git checkout master
git pull origin master
bumpversion $1
python setup.py sdist bdist_wheel

CURRENT_VERSION=`python -c "import slackly; print(slackly.__version__)"`

twine upload sdist/slackly-${CURRENT_VERSION}*
