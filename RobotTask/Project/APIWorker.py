import base64

import requests


class APIWorker(object):
    BASE_URL = "http://httpbin.org/"
    GET = "get"
    STREAM = "stream/%d"
    BASIC_AUTH = "basic-auth/%s/%s"
    COLON = ":"
    AUTHORIZATION = "Authorization"
    BASIC = "Basic "

    def __init__(self):
        self._base_url = self.BASE_URL

    def request_get(self):
        return requests.get(self._base_url + self.GET)

    def request_stream(self, number):
        return requests.get(self._base_url + self.STREAM % number)

    def request_basic_auth(self, valid_usr, valid_pswd, actaul_usr, actual_pswd):
        authHeader = base64.b64encode(bytes(actaul_usr + self.COLON + actual_pswd, 'utf-8'))
        return requests.get(self._base_url + self.BASIC_AUTH % (valid_usr, valid_pswd), headers=
        {self.AUTHORIZATION: self.BASIC + authHeader})
