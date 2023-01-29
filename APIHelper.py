# -*- coding: utf-8 -*-
import requests

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class APIHelper:
    def __init__(self):
        self.baseUrl = "http://movies.coralsundy.com:8080/v1/douyu"

    def request(self, action, param=None):
        reqUrl = self.baseUrl + action
        if param != None:
            reqUrl = reqUrl + "?" + urlencode(param)

        response = requests.get(reqUrl, timeout=5, verify=False)
        jsonObject = response.json()

        return jsonObject

