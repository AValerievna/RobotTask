from Project.APIWorker import APIWorker


class APIWorkerLibrary(object):
    def __init__(self):
        self._api_worker = APIWorker()
        self._res_resp = None

    def request_get(self, header_name, header_value):
        self._res_resp = self._api_worker.request_get(header_name, header_value)

    def request_stream(self, number):
        self._res_resp = self._api_worker.request_stream(number)

    def request_basic_auth(self, valid_usr, valid_pswd, actaul_usr, actual_pswd):
        self._res_resp = self._api_worker.request_basic_auth(valid_usr, valid_pswd, actaul_usr, actual_pswd)

    # def check_response(self, expected):
    #     if str(self._res_resp.status_code) != expected:
    #         raise AssertionError('%s != %s' % (self._res_resp.status_code, expected))

    def get_resp_status_code_str(self):
        return str(self._res_resp.status_code)

    def get_resp_header_str(self, header_name):
        return self._res_resp.json()['headers'][header_name]

    def get_resp_auth_str(self):
        return self._res_resp.json()['authenticated']

    def get_resp_user_str(self):
        return self._res_resp.json()['user']

    def get_resp_line_count_str(self):
        sum(chunk.count('\n')
            for chunk in iter(lambda: self._res_resp.json(), ''))
