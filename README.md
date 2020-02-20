# Unicorn-Embraces-Moon

# deployment

End state should be main.py called with a command name --test
This setup should be automated and checking github for changes and auto deploying based on that.

# application
code runs and tests the connection and then writes results to the DB.
the thought is that when a failure is detected we go ahead and reboot the device.
from there we'll have to figure out the wait time before we test again
