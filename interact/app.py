#!flask/bin/python
from flask import Flask, request, jsonify

from interact.interact_api import Interac

app = Flask(__name__)
interac_api = Interac()


@app.route('/interac/request-money', methods=["GET"])
def request_money():
    amount = request.args.get("amount")
    email = request.args.get("email")

    req_link = interac_api.send_money_request(amount, email)
    return jsonify({"request_link": req_link})


@app.route('/callbacks/transfer-completion', methods=["POST"])
def notification():
    print("i got transfer completion")
    print(request.data)


@app.route('/callbacks/transfer-creation', methods=["POST"])
def notification2():
    print("i got transfer creation")
    print(request.data)


@app.route('/notifications', methods=["POST"])
def notification3():
    print("i got notification")
    print(request.data)



if __name__ == '__main__':
    app.run(port=8000)
    # app.run(debug=True)