from interact import moneyRequests
import base64
import random #for salt
import hashlib
import interact.authentication as authentication
import uuid

class Interac:
    def __init__(self):
        secret_key  = 'ovxNE0bQNMBLxoR9vDXjQouB9z640q04LGYI5gVZtZM'
        self.salt = self._create_salt()
        key_and_salt = self.salt + ":" + secret_key
        self.encoded_key = self._encode_secret_key(key_and_salt)
        self.third_party_access_id = 'CA1TAFVkBhxeKE3x'
        self.api_registration_id = "CA1ARj9rFprAhWDd"
        self.device_id = "device_id: " + str(uuid.uuid4()) # random for now
        self.access_token = authentication.auth(self.salt, self.encoded_key, self.third_party_access_id)

    def send_money_request(self, amount, email):
        """ 
        
        :param amount float|int: 
        :param email: 
        :return str: url for the money request 
        """

        request_id = 'requestID'
        name = 'Tash-had Saqif'
        contact_id = 'CAb6354mWzEW'
        from_date = '2018-08-20T16:12:12.000Z'
        to_date = '2019-01-20T16:12:12.000Z'
        random_id = '34674366743hsvgkjvgskvb'

        response = moneyRequests.sendMoneyRequestOneTimeContact(self.access_token, self.third_party_access_id, request_id, self.device_id, self.api_registration_id, from_date, to_date, amount)
        return response["paymentGatewayUrl"]

    def get_money_request_status(self, reference_number):
        pass

    def _encode_secret_key(self, keyAndSalt):
        h = hashlib.sha256()
        h.update(keyAndSalt.encode())
        return base64.b64encode(h.digest()).decode("utf-8")

    def _create_salt(self):
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars = []
        for i in range(16):
            chars.append(random.choice(ALPHABET))

        return "".join(chars)
