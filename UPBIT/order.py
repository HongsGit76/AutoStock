"""
Name	설명	타입
market *	마켓 ID (필수)	String
side *	주문 종류 (필수)
- bid : 매수
- ask : 매도	String
volume *	주문량 (지정가, 시장가 매도 시 필수)	NumberString
price *	주문 가격. (지정가, 시장가 매수 시 필수)
ex) KRW-BTC 마켓에서 1BTC당 1,000 KRW로 거래할 경우, 값은 1000 이 된다.
ex) KRW-BTC 마켓에서 1BTC당 매도 1호가가 500 KRW 인 경우, 시장가 매수 시 값을 1000으로 세팅하면 2BTC가 매수된다.
(수수료가 존재하거나 매도 1호가의 수량에 따라 상이할 수 있음)	NumberString
ord_type *	주문 타입 (필수)
- limit : 지정가 주문
- price : 시장가 주문(매수)
- market : 시장가 주문(매도)	String
identifier	조회용 사용자 지정값 (선택)	String (Uniq 값 사용)
"""

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

query = {
    'market': 'KRW-BTC',
    'side': 'bid',
    'volume': '0.01',
    'price': '100.0',
    'ord_type': 'price',
}
query_string = urlencode(query).encode()

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

# payload = {
#     'access_key': access_key,
#     'nonce': str(uuid.uuid4()),
#     'query_hash': query_hash,
#     'query_hash_alg': 'SHA512',
# }

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.post(server_url + "/v1/orders", params=query, headers=headers)