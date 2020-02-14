# Unicorn-Embraces-Moon

# deployment
- automate deployments with a cron job or other mechanism
- manual steps :
python3 virtualenv setup
cron job setup
sqlite3 database setup
nginx setup with gunicorn, setup gunicord systemd https://docs.gunicorn.org/en/stable/deploy.html

# how do I think this is going to work

CRON JOB & DB FU

The CRON job runs every 5 minutes.
Checks DB for what action to take.

if power off signal is on
if 200 response back from > 50% of all sites listed to test
record results to the DB as a ++ pass or a -- failed

if power off signal is on
check if number of internet connection tests has a failed number > 0 and < 6
run test internet connection

if power off signal is on
if number of internet connection tests has a failed number > 0 and >= 6
send power off signal to internet

if power off signal is off, then turn it on