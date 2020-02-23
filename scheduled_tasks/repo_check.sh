#!/bin/bash

# Terminal Colors
ACTION='\033[1;90m'
FINISHED='\033[1;96m'
READY='\033[1;92m'
NOCOLOR='\033[0m'
ERROR='\033[0;31m'

# Checking remote if it's there and fetching head
echo -e ${ACTION}Checking Git Repo
git remote -v
git fetch

# Getting Status
echo -e ${ACTION}Checking Repo Is Up To Date
STATUS=`git status`
echo -e =======================${NOCOLOR}

# Signal to git pull or not
UPDATED="branch is up to date"
NOT_UPDATED="branch is behind"

# If repo current then no action needed
if [[ "$STATUS" == *"$UPDATED"* ]]; then
    echo -e ${FINISHED} Repo is ${UPDATED} ${NOCOLOR}
fi

# If not updated then we need to update
if [[ "$STATUS" == *"$NOT_UPDATED"* ]]; then
    echo -e ${ERROR} Repo is Not Updated. ${NOCOLOR}
    
    echo -e ${ACTION} Updating the repo ${NOCOLOR}
    git pull
    echo -e ${FINISHED} Now Repo Is Updated
    echo -e =======================${NOCOLOR}

    echo -e ${ACTION} Copying new cron job files
    sudo cp ./*.cron /etc/cron.d/
    sudo chmod 644 /etc/cron.d/*.cron
    echo -e ${FINISHED} Files copied over 
    echo -e =======================${NOCOLOR}
    
    echo -e ${ACTION} Python environment setup
    cd /home/pi/Unicorn-Embraces-Moon
    python3 -m venv env
    ./env/bin/python3 -m pip install -r requirements.txt
    echo -e ${FINISHED} Python Environment Setup/Update Complete 
    echo -e =======================${NOCOLOR}
fi

