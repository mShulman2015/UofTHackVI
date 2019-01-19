#!flask/bin/python
from flask import Flask, request, jsonify

from interact.interact_api import send_money_request

app = Flask(__name__)


@app.route('/interac/request-money', methods=["GET"])
def request_money():
    amount = request.args.get("amount")
    email = request.args.get("email")

    req_link = send_money_request(amount, email)
    return jsonify({"request_link": req_link})


@app.route('/interac/notifications', methods=["POST"])
def notification():
    print("i got called")
    print(request.data)


if __name__ == '__main__':
    app.run(port=8000)
    # app.run(debug=True)