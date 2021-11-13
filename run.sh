#!/bin/bash
pip3 install ./requirements.txt
export FLASK_APP=./scripts/pi-433
flask run --host=0.0.0.0