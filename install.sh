#!/bin/bash
# Copy wrapper to the init directory
cp ./Pi433Daemon.conf /etc/init/Pi433Daemon.conf

# Read out the current path
PWD=`pwd`

# Change the path in the config file
sed -i -e 's/___PATH___/$PWD/g' /etc/init/Pi433Daemon.conf

# Check the config
init-checkconf /etc/init/Pi433Daemon.conf