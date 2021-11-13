#!/bin/bash
# Read out the current path
PWD=$(pwd)

# Change the path in the config file
sed "s|___PATH___|${PWD}|g" ./Pi433Daemon.conf > /etc/init/Pi433Daemon.conf

# reboot the system
reboot