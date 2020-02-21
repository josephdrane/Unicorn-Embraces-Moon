# Unicorn-Embraces-Moon


## deployment summary

End state should be main.py called with a command name --test
This setup should be automated and checking github for changes and auto deploying based on that.


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


## what's the hardware here?

Soldering Iron
Cables
Longer Power Cable
Screws to mount
32G Samsung MicroSD Card
Raspbian Pi OS

Digital Loggers IoT Power Relay -
![Digital Loggers IoT Power Relay](http://www.digital-loggers.com/iot.jpg)

Raspberry Pi Zero W - 
[Amazon](https://www.amazon.com/Vilros-Raspberry-Kit-Premium-Essential-Accessories/dp/B0748NK116)
![VilrosRaspberryPiZeroW](https://images-na.ssl-images-amazon.com/images/I/91V-bnJcEWL._SL1500_.jpg)

