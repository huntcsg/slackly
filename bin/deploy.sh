#!/usr/bin/env bash

# Let's die if we have an error
set -e

cd ../deploy

# Activate the build/deploy virtualenv
source venv/bin/activate

# Install the two things we need to make this work
pip install --upgrade bumpversion twine >> /dev/null 2>&1

# Get rid of the "new" directory
if [ -e new ];
then
    echo "Remove directory <new>"
    rm -rf new
fi

echo "Cloning slackly"
git clone https://github.com/huntcsg/slackly.git new >> /dev/null 2>&1

cd new

# Get the old version from the setup.cfg
OLD_VERSION=`python -c "import configparser; c=configparser.RawConfigParser(); c.read('setup.cfg'); print(c.get('bumpversion', 'current_version'));"`

# We are going to bump the version and then
# push to the origin repo
echo "Bumping version ($1)"
bumpversion $1

# Let's build the package and upload it to pypi
python setup.py sdist bdist_wheel  >> /dev/null 2>&1

CURRENT_VERSION=`python -c "import configparser; c=configparser.RawConfigParser(); c.read('setup.cfg'); print(c.get('bumpversion', 'current_version'));"`

echo "Uploading to twine"
twine upload dist/slackly-${CURRENT_VERSION}*

# If we succeeded, let's push to github with the new commits and tags
echo "Pushing to github with new version and tag"
git push --tags origin master


cd ..

echo "Shuffling directories"
if [ -e latest ];
then
    if [ -e "$OLD_VERSION" ];
    then
        echo "old version <$OLD_VERSION> already saved. Something probably went wrong."
    else
        mv latest $OLD_VERSION
    fi
fi
mv new latest
