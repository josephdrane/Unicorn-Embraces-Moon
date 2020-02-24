#!/bin/bash

ACTION='\033[1;90m'
FINISHED='\033[1;96m'
READY='\033[1;92m'
NOCOLOR='\033[0m'
ERROR='\033[0;31m'
 
# Getting Status
echo -e ${ACTION}Testing Internet${NOCOLOR}

/home/pi/Unicorn-Embraces-Moon/env/bin/python3 main.py --test

echo -e ${FINISHED}=======================${NOCOLOR}
