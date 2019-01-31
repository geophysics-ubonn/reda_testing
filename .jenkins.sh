# This file is called by jenkins.

echo "Starting automatic build #$BUILD_NUMBER on" `date`
start=$(date +"%s")

# Show last change to repo in build log
echo `git log -1 --pretty="Last change by %cn (%h): %B"`

# link python to python3 (Debian issue)
ln -sf /usr/bin/python3 python
export PATH=`pwd`:$PATH

# Install latest version of reda in local folder
URL="https://github.com/geophysics-ubonn/reda"
FOLDER="reda"

if [ ! -d "$FOLDER" ] ; then
    git clone $URL $FOLDER
else
    cd "$FOLDER"
    git pull $URL
    cd ..
fi

export PYTHONPATH="./reda/lib":$PYTHONPATH

# Main test
pytest -v
