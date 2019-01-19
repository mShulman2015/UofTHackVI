#!flask/bin/python
import psycopg2
from flask import Blueprint, Flask, request, jsonify
from interact.interac_api import Interac
import threading
import atexit

conn = psycopg2.connect(database = "instacar", user = "instacar", password="instacar", host = "127.0.0.1", port = "5432")

interac_api_controller_bp = Blueprint("interac_api_controller", __name__)
interac_api = Interac()

POOL_TIME = 30 # Seconds

# variables that are accessible from anywhere
unfulfilled_payment_requests = {}

# lock to control access to variable
data_lock = threading.Lock()

# thread handler
check_completed_payments_thread = threading.Thread()


def _interrupt():
    global check_completed_payments_thread
    check_completed_payments_thread.cancel()


def _check_unfulfilled_requests():
    global unfulfilled_payment_requests
    global check_completed_payments_thread
    with data_lock:
        print("data_lock")
        cur = conn.cursor()
        cur.execute("SELECT reference_num, cid from payment where fufilled='f'")
        rows = cur.fetchall()
        for row in rows:
            reference_num = row[0]
            car_id = row[1]
            money_req = interac_api.get_money_request(reference_num)

            if money_req["status"] == 7 or money_req["status"] == 3:
                print(money_req, "\n")
                cur = conn.cursor()
                cur.execute("UPDATE payment SET fufilled='t' WHERE reference_num='{}'".format(reference_num))
                #TODO: unlock car

    # Set the next thread to happen
    check_completed_payments_thread = threading.Timer(POOL_TIME, _check_unfulfilled_requests, ())
    check_completed_payments_thread.start()


def fetch_and_process_fulfilled_requests():
    global check_completed_payments_thread, unfulfilled_payment_requests
    # unfulfilled_payment_requests = interac_api.get_unfulfilled_payment_requests()
    check_completed_payments_thread = threading.Timer(POOL_TIME, _check_unfulfilled_requests, ())
    check_completed_payments_thread.start()

fetch_and_process_fulfilled_requests()
atexit.register(_interrupt)
app = Flask(__name__)


@interac_api_controller_bp.route('/request-money', methods=["GET"])
def request_money():
    amount = request.args.get("amount")
    email = request.args.get("email")

    req_link = interac_api.send_money_request(amount, email)
    return jsonify({"request_link": req_link})


@interac_api_controller_bp.route('/callbacks/transfer-completion', methods=["POST"])
def notification():
    print("i got transfer completion")
    print(request.data)


@interac_api_controller_bp.route('/callbacks/transfer-creation', methods=["POST"])
def notification2():
    print("i got transfer creation")
    print(request.data)


@interac_api_controller_bp.route('/notifications', methods=["POST"])
def notification3():
    print("i got notification")
    # print(request.data)
    return {}

# if __name__ == '__main__':
#     app.run(port=8000)
#     # app.run(debug=True)