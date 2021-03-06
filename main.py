from flask import Flask, redirect, request, jsonify, send_from_directory
from flask_cors import CORS

import psycopg2

from interact.interac_api_controller import interac_api_controller_bp
from smartCar.smartcar_api_controller import smartcar_api_controller_bp

app = Flask(__name__,
            static_url_path='',
            static_folder='static')
cors = CORS(app, resources={r"/*/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(interac_api_controller_bp, url_prefix="/interac")
app.register_blueprint(smartcar_api_controller_bp, url_prefix="/smartcar")


conn = psycopg2.connect(database = "instacar", user = "instacar", password="instacar", host = "127.0.0.1", port = "5432")
print("Opened database successfully")


@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')


@app.route('/submit_login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or password is None or len(email) == 0 or len(password) == 0:
        return redirect('/')

    cur = conn.cursor()
    cur.execute("SELECT uid from user_tbl where email=\'{}\' and passwrod=\'{}\'".format(email, password))
    rows = cur.fetchall()
    if rows is None or len(rows) == 0:
        return redirect('/')
    return redirect('/select_car.html')


@app.route('/api/select_car', methods=['GET'])
def get_cars():
    cur = conn.cursor()
    cur.execute("SELECT cid, make, model, year from car where in_use='false'")
    rows = cur.fetchall()
    g = []
    for row in rows:
        g.append({
            "cid": row[0],
            "make": row[1],
            "model": row[2],
            "year": row[3]
            })
    return jsonify(g)


@app.route('/select/<int:cid>', methods=["GET"])
def select_car(cid):
    # TODO: add call to make interac payment
    return "Thank your for purchasing a car, please accept the payment request, and the car will be opened for you"

if __name__ == '__main__':
    app.run(port=8000)
