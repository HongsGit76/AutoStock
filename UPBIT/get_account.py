import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

import config.Config as cf

access_key = cf.Config.ACCESS_KEY
secret_key = cf.Config.SECRET_KEY
server_url = cf.Config.SERVER_URL

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())