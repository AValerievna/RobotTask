from ..Project.APIWorker import APIWorker


class APIWorkerLibrary(object):
    def __init__(self):
        self._api_worker = APIWorker()
        self._res_resp = None

    def request_get(self):
        self._res_resp = self._api_worker.request_get()

    def request_stream(self, number):
        self._res_resp = self._api_worker.request_stream(number)

    def request_basic_auth(self, valid_usr, valid_pswd, actaul_usr, actual_pswd):
        self._res_resp = self._api_worker.request_basic_auth(valid_usr, valid_pswd, actaul_usr, actual_pswd)

    def check_response(self, expected):
        if self._res_resp.status_code != expected:
            raise AssertionError('%s != %s' % (self._res_resp, expected))
