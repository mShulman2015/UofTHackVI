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
        # name = 'Tash-had Saqif'
        # contact_id = 'CAb6354mWzEW'
        from_date = '2018-08-20T16:12:12.000Z'
        to_date = '2019-01-20T16:12:12.000Z'
        # random_id = '34674366743hsvgkjvgskvb'

        response = moneyRequests.sendMoneyRequestOneTimeContact(self.access_token, self.third_party_access_id, request_id, self.device_id, self.api_registration_id, from_date, to_date, amount)
        print("Payment request response:", response)
        if "paymentGatewayUrl" in response:
            return response["paymentGatewayUrl"]
        return {}

    def get_money_request(self, reference_number=None):
        request_id = str(uuid.uuid4())
        print("REQUEST ID AND REF NUM", request_id, reference_number)
        data =  moneyRequests.getMoneyRequest(self.access_token, self.third_party_access_id, request_id, self.device_id, self.api_registration_id, referenceNumber=reference_number)
        print("DATA", data)
        return data

    def process_payment_notification(self, payment_data):
        for update in payment_data["moneyRequestUpdates"]:
            if update["state"] == "REQUEST_FULFILLED":
                from smartCar.smartcar_api_controller import unlock_vehicle
                unlock_vehicle(self.get_vehicle_id_with_payment_request_id(update["sourceMoneyRequestId"]))

    def get_vehicle_id_with_payment_request_id(self, payment_request_id):
        # TODO: Look at DB to see which vehicle ID is associated with the given payment request ID
        # That will tell us which car the user has paid for. Make sure to store the requested car prior to sending the payment request
        return "c4550682-1f76-4954-969d-6df89204c5ae"

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
    print(i.get_money_request('CA1MRdb2Brva'))
