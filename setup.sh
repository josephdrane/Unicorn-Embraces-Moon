#!/bin/bash

# Terminal Colors
ACTION='\033[1;90m'
FINISHED='\033[1;96m'
READY='\033[1;92m'
NOCOLOR='\033[0m'
ERROR='\033[0;31m'


# UPDATING SERVER
echo -e ${ACTION} UPDATING SERVER
echo -e =======================${NOCOLOR}
sudo apt-get update -y
echo -e 


# INSTALL GIT & VENV
echo -e ${ACTION} INSTALL GIT & VENV
echo -e =======================${NOCOLOR}
sudo apt-get install git python3-venv
echo -e 


# SSH Key
echo -e ${ACTION} Checking SSH Key For Git Access
echo -e =======================${NOCOLOR}
id_rsa_pub=~/.ssh/id_rsa.pub
if test -f "$id_rsa_pub"; then
    echo -e ${FINISHED} SSH Public Key $id_rsa_pub exists! ${NOCOLOR}
    cat $id_rsa_pub
else
    echo -e ${ERROR} SSH Key Not Found : $id_rsa_pub ${NOCOLOR}
    echo -e ${ACTION} Creating Key
    ssh-keygen -b 2048 -t rsa -q -N ""
    if test -f "$id_rsa_pub"; then
        echo -e ${FINISHED} SSH Public Key $id_rsa_pub exists!
        cat $id_rsa_pub
    else
        echo -e ${ERROR} SSH Key creation failed : $id_rsa_pub
fi
echo -e =======================${NOCOLOR}
echo -e 


# Setup Python Virtual Environment
echo -e ${ACTION} Setup Python Virtual Environment
echo -e =======================${NOCOLOR}
cd ~/unicorn-embraces-moon
python3 -m virtualenv env
./env/bin/python3 -m pip install -r requirements.txt
echo -e


# CRON Job Setup
echo -e ${ACTION} SETUP CRON JOBS
echo -e =======================${NOCOLOR}
chmod +x ./scheduled_tasks/repo_check.sh
chmod +x ./scheduled_tasks/test_internet.sh

cp ./scheduled_tasks/repo_check.cron /etc/cron.d/
cp ./scheduled_tasks/test_internet.cron /etc/cron.d/

chmod 644 /etc/cron.d/repo_check.cron
chmod 644 /etc/cron.d/test_internet.cron


# FINISHED
echo -e ${FINISHED} FINISHED
echo -e =======================${NOCOLOR}