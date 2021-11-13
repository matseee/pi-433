#!/bin/bash
# Read out the current path
PWD=$(pwd)

# Change the path in the config file
sed "s|___PATH___|${PWD}|g" ./Pi433.service > /etc/systemd/system/Pi433.service

# Enable service
systemctl enable Pi433.service
systemctl daemon-reload

# Start service
systemctl start Pi433.service