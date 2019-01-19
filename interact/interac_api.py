from interact import moneyRequests
import base64
import random #for salt
import hashlib
import interact.authentication as authentication
import uuid

class Interac:
    def __init__(self):
        secret_key  = 'JHtQapvZ8XWhE9Y64hct1FzgPBI6sJ9EmjKooZ77fUo'
        self.salt = self._create_salt()
        key_and_salt = self.salt + ":" + secret_key
        self.encoded_key = self._encode_secret_key(key_and_salt)
        self.third_party_access_id = 'CA1TAvDumQxCGSnC'
        self.api_registration_id = "CA1ARQkp358AXyYF"
        self.device_id = "device_id: " + str(uuid.uuid4()) # random for now
        self.access_token = authentication.auth(self.salt, self.encoded_key, self.third_party_access_id)

    def send_money_request(self, amount, email):
        """ 
        
        :param amount float|int: 
        :param email: 
        :return str: url for the money request 
        """

        request_id = str(uuid.uuid4())
        name = 'Tash-had Saqif'
        contact_id = 'CAb6354mWzEW'
        from_date = '2018-08-20T16:12:12.000Z'
        to_date = '2019-01-20T16:12:12.000Z'
        random_id = '34674366743hsvgkjvgskvb'

        response = moneyRequests.sendMoneyRequestOneTimeContact(self.access_token, self.third_party_access_id, request_id, self.device_id, self.api_registration_id, from_date, to_date, amount)
        print("Payment request response:", response)
        if "paymentGatewayUrl" in response:
            return response["paymentGatewayUrl"]
        return {}

    def get_money_request(self, reference_number=None):
        request_id = str(uuid.uuid4())

        return moneyRequests.getMoneyRequest(self.access_token, self.third_party_access_id, request_id, self.device_id, self.api_registration_id, referenceNumber=reference_number)
        return data[0]

    def get_unfulfilled_payment_requests(self):
        return "a"

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

if __name__ == "__main__":
    i = Interac()
    print(i.get_money_request('CA1MRZxJR4Ze'))
