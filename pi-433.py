#!/usr/bin/env python3

import logging

from flask import Flask, request
from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)


class Endpoint:
    def __init__(self, name, on, off, state):
        self.name = name
        self.on = on
        self.off = off
        self.state = 0


endpoints = []
endpoints.append(Endpoint('A', 1361, 1364, 0))
endpoints.append(Endpoint('B', 4433, 4436, 0))
endpoints.append(Endpoint('C', 5201, 5204, 0))
endpoints.append(Endpoint('D', 5393, 5396, 0))

app = Flask(__name__)


def getEndpoint(name):
    for endpoint in endpoints:
        if endpoint.name == name:
            return endpoint
    return None


@app.route('/<endpointName>', methods=['GET'])
def get(endpointName):
    endpoint = getEndpoint(endpointName)
    return '{ "state":"' + str(endpoint.state) + '" }'


@app.route('/<endpointName>', methods=['POST'])
def set(endpointName):
    request_data = request.get_json()
    new_state = request_data['state']

    endpoint = getEndpoint(endpointName)

    logging.info('Set ' + endpointName + ' = ' + str(new_state))
    endpoint.state = new_state

    if new_state == 1:
        code = endpoint.on
    else:
        code = endpoint.off

    if code is not None:
        rfdevice = RFDevice(17)
        rfdevice.enable_tx()
        rfdevice.tx_repeat = 50
        rfdevice.tx_code(code, 1, 350, 24)
        rfdevice.cleanup()
        logging.info('Send code ' + str(code))
        return '{}'
    else:
        logging.info('Endpoint not found: ' + endpointName)
        abort(404)
        return '404 Endpoint not found'
