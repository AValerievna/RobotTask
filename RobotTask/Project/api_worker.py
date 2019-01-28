import requests


class APIWorker(object):
    BASE_URL = "http://httpbin.org/"
    GET = "get"
    STREAM = "stream/%s"
    BASIC_AUTH = "basic-auth/%s/%s"
    COLON = ":"
    AUTHORIZATION = "Authorization"
    BASIC = "Basic "

    def __init__(self):
        self._base_url = self.BASE_URL

    def request_get(self, header_name, header_value):
        return requests.get(self._base_url + self.GET, headers={header_name: header_value})

    def request_stream(self, number):
        return requests.get(self._base_url + self.STREAM % number)

    def request_basic_auth(self, valid_usr, valid_password, actual_usr, actual_password):
        return requests.get(self._base_url + self.BASIC_AUTH % (valid_usr, valid_password),
                            auth=(actual_usr, actual_password))
