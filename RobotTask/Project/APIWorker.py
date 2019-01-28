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

    def request_basic_auth(self, valid_usr, valid_pswd, actual_usr, actual_pswd):
        return requests.get(self._base_url + self.BASIC_AUTH % (valid_usr, valid_pswd), auth=(actual_usr, actual_pswd))
        # authHeader = base64.b64encode(bytes(actaul_usr + self.COLON + actual_pswd, 'utf-8'))
        # return requests.get(self._base_url + self.BASIC_AUTH % (valid_usr, valid_pswd), headers=
        # {self.AUTHORIZATION: self.BASIC + authHeader})
