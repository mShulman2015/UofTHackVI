import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import os
import json

app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None
access_token = None
refresh_token = None

client = smartcar.AuthClient(
    client_id="ddfe836a-9f54-4fb2-8d16-9d70059b9dcd",
    client_secret="431cb198-322d-4f4c-a38c-2a2a37d9b19f",
    redirect_uri="http://localhost:8000/exchange",
    scope=['read_vehicle_info','read_location', 'control_security', 'control_security:unlock', 'control_security:lock'],
    test_mode=True,
)

def get_token():
    file = open("tokens.txt", 'r')
    global access_token
    global refresh_token
    access_token = file.readline().strip()
    refresh_token = file.readline().strip()
    print(access_token)
    print(refresh_token)
    file.close()

def set_tokens(access, refresh):
    file = open('tokens.txt', 'w')
    file.write(access+"\n")
    file.write(refresh)
    file.close()

    #setting variables to the new codes
    global access_token
    global refresh_token
    access_token = access
    refresh_token = refresh

get_token()

@app.route('/token', methods=['POST'])
def token():
    get_token()
    print(refresh_token)
    print(access_token)
    code = client.exchange_refresh_token(refresh_token)
    print(code)
    set_tokens(code['access_token'], code['refresh_token'])
    return jsonify(code)

@app.route('/login', methods=['GET'])
def login():
    # TODO: Authorization Step 1b: Launch Smartcar authentication dialog
    auth_url = client.get_auth_url()
    return redirect(auth_url)

@app.route('/exchange', methods=['GET'])
def exchange():
    code = request.args.get('code')
    #code="efc907c2-11ba-49fa-a236-294282e3b429"
    print(code)

    # TODO: Request Step 1: Obtain an access token
    # access our global variable and store our access tokens
    global access
    global access_token
    global refresh_token
    # in a production app you'll want to store this in some kind of
    # persistent storage
    access = client.exchange_code(code)
    print(access)
    access_token = access['access_token']
    refresh_token = access['refresh_token']
    print(access_token)
    print(refresh_token)
    return '', 200

@app.route('/vehicle', methods=['GET'])
def vehicle():
    global access_token
    global refresh_token
    get_token()
    print(access_token)
    vehicle_ids = smartcar.get_vehicle_ids(access_token)['vehicles']

    #instantiate the first vehicle in the vehicle id list

    vehicle = smartcar.Vehicle(vehicle_ids[0], access_token)

    # TODO: Request Step 4: Make a request to Smartcar API
    info = vehicle.info()
    print(info)
    '''
    {
        "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
        "make": "TESLA",
        "model": "Model S",
        "year": 2014
    }
    '''
    print()

    return jsonify(info)

@app.route('/unlock', methods=['POST'])
def unlock():
    pass

@app.route('/location', methods=['GET'])
def location():
    #1d3bb4b5-ddeb-492e-974b-43e5dfa68fdd
    global access_token
    global refresh_token
    get_token()
    print(access_token)
    vehicle_ids = smartcar.get_vehicle_ids(access_token)['vehicles']
    print("The cars")
    print(vehicle_ids)
    #instantiate the first vehicle in the vehicle id list
    #vehicle = smartcar.Vehicle(vehicle_ids[0], access_token)
    data = []
    for element in vehicle_ids:
        vehicle = smartcar.Vehicle(element, access_token)
        data.append([element, vehicle.location()])
    # TODO: Request Step 4: Make a request to Smartcar API
    # location = vehicle.location()
    # print(location)
    print(data)
    '''
    {
        "id": "36ab27d0-fd9d-4455-823a-ce30af709ffc",
        "make": "TESLA",
        "model": "Model S",
        "year": 2014
    }
    '''
    print()

    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8000)
