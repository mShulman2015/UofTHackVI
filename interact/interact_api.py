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

    def get_money_request(self, reference_number=None):
        request_id = 'requestID'

        data = moneyRequests.getMoneyRequest(self.access_token, self.third_party_access_id, request_id, self.device_id, self.api_registration_id, referenceNumber=reference_number)
        return data[0]

    def get_unfulfilled_payment_requests(self):
        return [{"referenceNumber":"CA1MRSQubUV2","sourceMoneyRequestId":"240c6e01cb104b6da147b078e8ae1d5e","requestedFrom":{"contactId":"CAPshm37AKSk","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T18:34:14.821Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRddNY4mS","sourceMoneyRequestId":"824355d7942e49b59bf4ca6f40b8079a","requestedFrom":{"contactId":"CACmQkfqprJZ","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:48:19.080Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRe54Uat4","sourceMoneyRequestId":"253e295f640f480c95fc9f53b14b53db","requestedFrom":{"contactId":"CAZJXbZT7mg9","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:46:54.932Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRagcWfUA","sourceMoneyRequestId":"070a27d42ca04129a128cbe3e148117c","requestedFrom":{"contactId":"CASqZ9fXhK7G","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:06:21.588Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRdV9XMqv","sourceMoneyRequestId":"df005579a11f4247b3a285cbb875f4e3","requestedFrom":{"contactId":"CAwpUPyKYrps","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:06:19.568Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRmAYee8g","sourceMoneyRequestId":"2d322c0a1e874d52bbb475eee7fc5fc6","requestedFrom":{"contactId":"CA9bUYQk32vt","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:05:22.184Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRec8ncsv","sourceMoneyRequestId":"2103e3cbb5f840febed0c283e5f5b8e3","requestedFrom":{"contactId":"CA6xjrTTXwNJ","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:02:03.866Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRFtTzXE9","sourceMoneyRequestId":"621729618b9b46c7ad01ce23067533e4","requestedFrom":{"contactId":"CAGwjngqYV5f","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:02:01.905Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRkGYN6DC","sourceMoneyRequestId":"2a04725d9483454782008fbeddbdf2a7","requestedFrom":{"contactId":"CA3FB5Ad4Dg9","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:01:46.757Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRqWXs7zX","sourceMoneyRequestId":"c2a4f7669473491fa5db5d250230c847","requestedFrom":{"contactId":"CAUK3FvEaD84","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:01:44.851Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MR7yWV47r","sourceMoneyRequestId":"6b0b2bb51d6846e8bf903c80b5e9e3ed","requestedFrom":{"contactId":"CANhuFnAaQZW","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:01:20.518Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRCRaZs5J","sourceMoneyRequestId":"843d72ed82a440fa9a35cf10eb7e437b","requestedFrom":{"contactId":"CAZ9SCnkNSdQ","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:01:18.500Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRgTQFfxC","sourceMoneyRequestId":"9d72aaedb5164727a200c246c8442433","requestedFrom":{"contactId":"CAMZqwjUSkN8","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:00:10.137Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MR69GAHCj","sourceMoneyRequestId":"1a42e68f98cf48459fdd6c2272004ec4","requestedFrom":{"contactId":"CAAzcYEuVyWj","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T15:00:07.832Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRB3bGnZh","sourceMoneyRequestId":"b7953805f9e74b22b318eafebd4d496c","requestedFrom":{"contactId":"CAvp7NUKfKb9","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T10:09:24.724Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRzNXjU36","sourceMoneyRequestId":"b76a937cd5db49e9a738daa3d2defe0c","requestedFrom":{"contactId":"CAU5CkjvQtz4","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T10:02:09.081Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRVJBTfvF","sourceMoneyRequestId":"733de10f52654e09a32f8d04d225f272","requestedFrom":{"contactId":"CAQZdqJb9Je5","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:58:12.926Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRDU2Q6y2","sourceMoneyRequestId":"bba7c3d2d12f4f87b5a6927349f202fe","requestedFrom":{"contactId":"CAkBYgJaSyUA","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:53:52.342Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRF2Z32wE","sourceMoneyRequestId":"0b0e76bcf42d4d6387ca83670b8da5c9","requestedFrom":{"contactId":"CAfQUKbjPEay","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:46:52.447Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRXx6sNTB","sourceMoneyRequestId":"ce17f53fe7004c7b9f40c51dc36200c9","requestedFrom":{"contactId":"CAKzpFyddeNG","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:44:04.621Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MR9PW2jPY","sourceMoneyRequestId":"578e32c9edda40b49af189d6cd931d8c","requestedFrom":{"contactId":"CAEyBVR9D7Ss","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:41:46.663Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRYGgRNea","sourceMoneyRequestId":"b946f97158e64d59b82f2946f7aab61d","requestedFrom":{"contactId":"CAfBHxp4ZkFk","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:39:06.884Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRwCqaFXH","sourceMoneyRequestId":"cf22ad29865d46a7ab110e3e147270cb","requestedFrom":{"contactId":"CAKGAHmqVtej","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:34:54.509Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRgNCYhGh","sourceMoneyRequestId":"495bf84c830e4b9da4b8c4a1bd219c88","requestedFrom":{"contactId":"CAspFbukvFBP","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:33:08.776Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRUNAvhu2","sourceMoneyRequestId":"60a50f58c70342e89eb00a5f78e21a84","requestedFrom":{"contactId":"CAsY4MXjEfKf","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:32:56.345Z","status":2,"notificationStatus":0},{"referenceNumber":"CA1MRyPXJvkV","sourceMoneyRequestId":"597ef4725972485692c159f8f0053255","requestedFrom":{"contactId":"CA8Xjuqya5f4","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":False,"creationDate":"2019-01-19T09:32:37.024Z","status":7,"notificationStatus":0},{"referenceNumber":"CA1MRkkWQbEW","sourceMoneyRequestId":"8dad528dff2748858a188b5c5f450449","requestedFrom":{"contactId":"CANJN8zSK7tJ","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T08:52:06.582Z","status":7,"notificationStatus":1},{"referenceNumber":"CA1MRQVNf2g2","sourceMoneyRequestId":"b074860e0a9c4501827bf86d6a887dfe","requestedFrom":{"contactId":"CAhRtexMxURT","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T08:17:43.058Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRG2vAgEZ","sourceMoneyRequestId":"afe1630c30994aa8ae955adc9aadec9d","requestedFrom":{"contactId":"CAzJyXE5EqBN","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":68.2,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T08:06:02.684Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRDMe6uCx","sourceMoneyRequestId":"34e9b3126dfb423381f98dba9fd268bf","requestedFrom":{"contactId":"CAb7EjuFhjHK","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:24:51.157Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MR7tNzfCR","sourceMoneyRequestId":"af83d16ef79941f8a420429079336340","requestedFrom":{"contactId":"CAZNyzsG8FkD","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:22:45.225Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRHTt6BSX","sourceMoneyRequestId":"1631220ccba74ff89dd7a6e0a595c819","requestedFrom":{"contactId":"CABCHvQW6ekJ","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:22:11.419Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRCZ8ZfU4","sourceMoneyRequestId":"43fe555ce9aa4302a1d3d6c5c9ec3773","requestedFrom":{"contactId":"CAqwHJZtHjxh","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:21:52.062Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRNahQsTp","sourceMoneyRequestId":"cefc0cd4accf451ab0767d3c9266856e","requestedFrom":{"contactId":"CAhkZcvFfm3F","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:19:25.551Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRDnZEyJM","sourceMoneyRequestId":"b0f44867478649a6b595bf52bee4cd25","requestedFrom":{"contactId":"CAAQeuPJMJqH","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:15:26.001Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRkh4t9pe","sourceMoneyRequestId":"38df17a02de54b39b9e48d0a4390b013","requestedFrom":{"contactId":"CAUf6DeMZrXN","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":50.4,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T06:13:42.362Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MR4mb288J","sourceMoneyRequestId":"b26adeeceec34f66b25fca3aebe4b968","requestedFrom":{"contactId":"CAYXmgQxT27b","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T05:51:03.901Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRHGpPhdE","sourceMoneyRequestId":"ffba3c0e8b3f4407a92d5163aa072f83","requestedFrom":{"contactId":"CA8jk6shn8WU","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T04:57:31.462Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRbUMBp7e","sourceMoneyRequestId":"16577116882340338f63985e04a96edd","requestedFrom":{"contactId":"CAwWDvcRgeRC","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T04:56:42.852Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MREvMmdrv","sourceMoneyRequestId":"b4d93c17c1234c85b84a707b97e114df","requestedFrom":{"contactId":"CAEWukSjUJZw","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T04:51:11.454Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRmsQAx5C","sourceMoneyRequestId":"b6bd6615d55048b5bee8c5c952faff8e","requestedFrom":{"contactId":"CAs8583PSbSe","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T04:51:05.479Z","status":2,"notificationStatus":1},{"referenceNumber":"CA1MRxVbx7jP","sourceMoneyRequestId":"b9e2360b9eb6473cb2fd104fb565494a","requestedFrom":{"contactId":"CAt6PYJnEGJk","contactName":"string","language":"en","notificationPreferences":[{"handle":"nanylagoon@gmail.com","handleType":"email","active":True}]},"amount":10,"currency":"CAD","editableFulfillAmount":False,"requesterMessage":"string","invoice":{"invoiceNumber":"string","dueDate":"2019-01-20T16:12:12.000Z"},"expiryDate":"2019-01-20T16:12:12.000Z","supressResponderNotifications":True,"creationDate":"2019-01-19T04:50:06.861Z","status":2,"notificationStatus":1}]

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
    i.get_money_request('CA1MRSQubUV2')