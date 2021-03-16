import requests

file_path = './market.json'

url = "https://api.upbit.com/v1/market/all"

querystring = {"isDetails":"false"}

response = requests.request("GET", url, params=querystring)

with open(file_path, 'w', encoding='UTF8') as outfile:
    outfile.write(response.text)