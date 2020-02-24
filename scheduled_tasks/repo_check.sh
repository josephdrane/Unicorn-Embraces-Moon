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
    echo -e =======================${NOCOLOR}
    echo -e
fi

# If not updated then we need to update
if [[ "$STATUS" == *"$NOT_UPDATED"* ]]; then
    echo -e ${ERROR} Repo is Not Updated. ${NOCOLOR}
    echo -e
    
    echo -e ${ACTION} Updating the repo ${NOCOLOR}
    git pull
    echo -e ${FINISHED} Now Repo Is Updated
    echo -e =======================${NOCOLOR}
    echo -e

    echo -e ${ACTION} Running Setup
    cd ../
    bash -c "setup.sh"
    echo -e =======================${NOCOLOR}
    echo -e
fi

