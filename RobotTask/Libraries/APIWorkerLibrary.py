from Project.api_worker import APIWorker


class APIWorkerLibrary(object):
    """
    library class for interaction of Robot Framework with API-service
    """

    NEW_LINE = '\n'
    USER = 'user'
    AUTHENTICATED = 'authenticated'
    HEADERS = 'headers'

    def __init__(self):
        self._api_worker = APIWorker()
        self._res_resp = None

    def request_get(self, header_name, header_value):
        """
        execute get request with a custom header

        header_name -- custom header name
        header_value -- custom header value
        """
        self._res_resp = self._api_worker.request_get(header_name, header_value)

    def request_stream(self, number):
        """
        execute stream request with <number> lines count

        number -- necessary number of lines
        """
        self._res_resp = self._api_worker.request_stream(number)

    def request_basic_auth(self, valid_usr, valid_password, actual_usr, actual_password):
        """
        execute basic authorization request

        valid_usr -- user name data in request URL
        valid_password -- user password data in request URL
        actual_usr  -- user name data in request header(which will be encoded)
        actual_password -- user password data in request header(which will be encoded)
        """
        self._res_resp = self._api_worker.request_basic_auth(valid_usr, valid_password, actual_usr,
                                                             actual_password)

    def get_resp_status_code_str(self):
        """
        :return response status code
        """
        return str(self._res_resp.status_code)

    def get_resp_header_str(self, header_name):
        """
        :return value of header <header_name> in response body
        """
        return self._res_resp.json()[self.HEADERS][header_name]

    def get_resp_auth_str(self):
        """
        :return 'authenticated' field of response body
        """
        return self._res_resp.json()[self.AUTHENTICATED]

    def get_resp_user_str(self):
        """
        :return 'user' field of response body
        """
        return self._res_resp.json()[self.USER]

    def get_resp_line_count_str(self):
        """
        :return count of response body lines
        """
        return self._res_resp.text.count(self.NEW_LINE)
