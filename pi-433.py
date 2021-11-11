#!/usr/bin/env python3

import logging

from flask import Flask
from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)


class Endpoint:
    def __init__(self, name, on, off):
        self.name = name
        self.on = on
        self.off = off


endpoints = []
endpoints.append(Endpoint('A', 1361, 1364))
endpoints.append(Endpoint('B', 4433, 4436))
endpoints.append(Endpoint('C', 5201, 5204))
endpoints.append(Endpoint('D', 5393, 5396))

rfdevice = RFDevice(17)
app = Flask(__name__)


def getCode(name, state):
    for endpoint in endpoints:
        if endpoint.name == name:
            if state == 1:
                return endpoint.on
            else:
                return endpoint.off
    return None


@app.route('/<endpointName>/<state>')
def handle(endpointName, state):
    logging.info('Set ' + endpointName + ' = ' + str(state))
    code = getCode(endpointName, state)

    if code is not None:
        rfdevice.enable_tx()
        rfdevice.tx_repeat = 50
        rfdevice.tx_code(code, 1, 350, 24)
        rfdevice.cleanup()
        logging.info('Send code ' + str(code))
    else:
        logging.info('Endpoint not found: ' + endpointName)
        abort(404)
