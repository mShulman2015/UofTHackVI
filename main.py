import smartcar
from flask import Flask, redirect, request, jsonify, send_from_directory
from flask_cors import CORS

import psycopg2
import os

app = Flask(__name__,
            static_url_path='',
            static_folder='static')
CORS(app)

conn = psycopg2.connect(database = "instacar", user = "instacar", password = "instacar", host = "174.138.109.226", port = "5432")
print "Opened database successfully"

@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/submit_login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None or len(email) == 0 or len(password) == 0:
        return redirect('/')

    return ''

if __name__ == '__main__':
    app.run(port=8000)
