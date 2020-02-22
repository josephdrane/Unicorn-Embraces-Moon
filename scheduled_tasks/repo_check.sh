#!/bin/bash

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

# If updated then we are good
if [[ "$STATUS" == *"$UPDATED"* ]]; then
    echo -e ${FINISHED} Repo is ${UPDATED} ${NOCOLOR}
fi

# If not updated then we need to update
if [[ "$STATUS" == *"$NOT_UPDATED"* ]]; then
    echo -e ${ERROR} Repo is Not Updated. Will update now ${NOCOLOR}
    git pull
    echo -e ${FINISHED} Now Repo Is Updated ${NOCOLOR}
fi

