import requests
import json
import pandas as pd
import urllib3
urllib3.disable_warnings()



def create_headers(host, credentials, token_headers, request_headers):
    print(credentials)
    # Sign in
    url = host+'/auth/signin'
    token = requests.post(url, json=credentials,headers=token_headers, verify=False)
    print(token.request.body)
    token_json = token.json()
    request_headers['Authorization'] = 'Bearer ' + token_json['token']
    headers = request_headers
    # print(headers)
    return headers
