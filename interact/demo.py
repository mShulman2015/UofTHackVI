import base64
import random #for salt
import hashlib
import string
import requests
import json

import interact.authentication as authentication
import interact.contacts as contacts
import interact.moneyRequests as moneyRequests

from time import gmtime, strftime

url2 = 'https://gateway-web.beta.interac.ca/publicapi/api/v2/'

def demo():
    
    secretKey  = 'KeEEtwGqWdLl5io73TAVehyOQ9-3hO9kZGcxaR0Tq6o'
    salt = createSalt()
    keyAndSalt = salt + ':' + secretKey
    thirdPartyAccessid = 'CA1TAFVkBhxeKE3x'
    requestId = 'requestID'
    deviceID = 'deviceID'
    apiRegistrationId = 'CA1ARj9rFprAhWDd'
    email = 'nanylagon@gmail.com'
    name = 'Tash-had Saqif'
    contactID = 'CAb6354mWzEW'
    encodedKey = encodeSecretKey(keyAndSalt)
    toDate = '2019-01-20T16:12:12.000Z'
    randomID = '34674366743hsvgkjvgskvb'
    fromDate = '2019-01-01T16:12:12.000Z'
    referenceNumber = 'CA1MRqNhTkFJ'

    print('starting')

    access_token = authentication.auth(salt, encodedKey, thirdPartyAccessid)

    # contacts.addContact(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, email, name)
    #contacts.getContacts(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId)
    #contacts.putContact(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, email, name, contactID)
    #contacts.deleteContact(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, contactID)
    #contacts.getContactThroughContactID(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, contactID)


    #money

    #moneyRequests.getMoneyRequest(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, fromDate, toDate)
    # moneyRequests.sendMoneyRequest(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, fromDate, toDate)
    # moneyRequests.sendMoneyRequestOneTimeContact(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId, fromDate, toDate)
    #moneyRequests.cancelMoneyRequests(access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId)
    #moneyRequests.noticeMoneyRequest(referenceNumber, access_token, thirdPartyAccessid, requestId, deviceID, apiRegistrationId)
    #moneyRequests.putMoneyRequest(referenceNumber, access_token, thirdPartyAccessid, requestId, deviceID,  apiRegistrationId, fromDate, toDate)
def encodeSecretKey(keyAndSalt):
    h = hashlib.sha256()
    h.update(keyAndSalt.encode())
    return base64.b64encode(h.digest()).decode("utf-8") 

def createSalt():
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chars=[]
    for i in range(16):
        chars.append(random.choice(ALPHABET))
    
    return "".join(chars)

