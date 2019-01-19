from interact import moneyRequests
import base64
import random #for salt
import hashlib
import interact.authentication as authentication
import uuid


def send_money_request(amount, email):
    """ 
    
    :param amount float|int: 
    :param email: 
    :return str: url for the money request 
    """
    secret_key  = 'KeEEtwGqWdLl5io73TAVehyOQ9-3hO9kZGcxaR0Tq6o'
    salt = _create_salt()
    key_and_salt = salt + ':' + secret_key
    third_party_access_id = 'CA1TAFVkBhxeKE3x'
    request_id = 'requestID'
    device_id = "device_id: " + str(uuid.uuid4())
    api_registration_id = 'CA1ARj9rFprAhWDd'
    name = 'Tash-had Saqif'
    contact_id = 'CAb6354mWzEW'
    encodedKey = _encode_secret_key(key_and_salt)
    to_date = '2019-01-20T16:12:12.000Z'
    random_id = '34674366743hsvgkjvgskvb'
    from_date = '2019-01-01T16:12:12.000Z'
    referenceNumber = 'CA1MRqNhTkFJ'

    access_token = authentication.auth(salt, encodedKey, third_party_access_id)
    response = moneyRequests.sendMoneyRequestOneTimeContact(access_token, third_party_access_id, request_id, device_id, api_registration_id, from_date, to_date, amount)
    return response["paymentGatewayUrl"]

def _encode_secret_key(keyAndSalt):
    h = hashlib.sha256()
    h.update(keyAndSalt.encode())
    return base64.b64encode(h.digest()).decode("utf-8")


def _create_salt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars = []
    for i in range(16):
        chars.append(random.choice(ALPHABET))

    return "".join(chars)

if __name__ == "__main__":
    req_link = send_money_request(50.4, "nanylagoon@gmail.com")
    print(req_link)