# Unicorn-Embraces-Moon


## deployment summary

End state should be main.py called with a command name --test
This setup should be automated and checking github for changes and auto deploying based on that.
I'll list out the steps and maybe someone could commit some code to automate the install / setup/ config.

### Pre-requisites : 
1. Pi has internet and update it
`sudo apt-get update -y`

2. GPIO pins and hardware have been tested from python (python interpreter is good)
Check out the `pinout` cli command.

3. install git and python venv
`sudo apt-get install git python3-venv -y`

4. create an ssh key, taking default prompts with:
`ssh-keygen`
I didn't do a passphrase

5. add ~/.ssh/id_rsa.pub to github or bitbucket or whatever for ssh access w/ out passwords
`cat .ssh/id_rsa.pub`
copy / paste output to SSH keys in your repo for access

6. setup the virtual environment
```
python3 -m virtualenv env
./env/bin/python3 -m pip install -r requirements.txt
```

### Deployment Setup : 




## application summary

code runs and tests the connection and then writes results to the DB.
the thought is that when a failure is detected we go ahead and reboot the device.
from there we'll have to figure out the wait time before we test again

**ADDED SUPPORT TO VIEW FAILED EASILY**
```python3 main.py --view```

## development setup

```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py --test
```


## what's needed to build something like this?

- Soldering Iron
- Cables
- Longer Power Cable
- Screws to mount
- 32G Samsung MicroSD Card
- doublesided velcro strips
- Raspbian Pi OS

- Digital Loggers IoT Power Relay -
![Digital Loggers IoT Power Relay](http://www.digital-loggers.com/iot.jpg)

- Raspberry Pi Zero W - 
[Amazon](https://www.amazon.com/Vilros-Raspberry-Kit-Premium-Essential-Accessories/dp/B0748NK116)
![VilrosRaspberryPiZeroW](https://images-na.ssl-images-amazon.com/images/I/91V-bnJcEWL._SL1500_.jpg)

