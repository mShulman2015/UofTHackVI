import smartcar
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

# global variable to save our access_token
access = None


@app.route('/login', methods=['GET'])
def login():
    auth_url = client.get_auth_url()
    return redirect(auth_url)
