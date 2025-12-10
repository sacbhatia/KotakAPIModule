from __future__ import absolute_import

import logging
import re
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from six.moves.urllib.parse import urlencode
from .exceptions import ApiException

# Try to use orjson for faster JSON, fallback to standard json
try:
    import orjson
    _json_dumps = lambda obj: orjson.dumps(obj).decode('utf-8')
    _json_loads = orjson.loads
except ImportError:
    import json
    _json_dumps = json.dumps
    _json_loads = json.loads


class RESTClientObject(object):
    __slots__ = ('configuration', '_json_pattern', '_form_pattern', 'session')
    
    """REST API Client

    This class is a client to perform requests to a REST API.

    Attributes:
        configuration (dict): configuration for the API client
    """

    def __init__(self, configuration):
        """
        Initialize the API client with a configuration dictionary.

        :param configuration: dictionary of configuration parameters
        """
        self.configuration = configuration
        # Pre-compile regex patterns for performance
        self._json_pattern = re.compile(r'json', re.IGNORECASE)
        self._form_pattern = re.compile(r'x-www-form-urlencoded', re.IGNORECASE)
        
        # Create session with connection pooling and retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"]
        )
        adapter = HTTPAdapter(
            pool_connections=10,
            pool_maxsize=20,
            max_retries=retry_strategy
        )
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def request(self, method, url, query_params=None, headers=None,
                body=None):
        """Perform a request to the REST API

        This method performs a request to the REST API using the provided parameters.

        :param method: HTTP request method (e.g. GET, POST, PUT)
        :param url: URL for the API endpoint
        :param query_params: (optional) query parameters for the API endpoint
        :param headers: (optional) headers for the API request
        :param body: (optional) request body for the API request
        :return: response from the API
        :raises: ApiException in case of a request error
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        headers = headers or {}

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            if method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if self._json_pattern.search(headers['Content-Type']):
                    request_body = None
                    if body is not None:
                        request_body = _json_dumps(body)
                    response = self.session.post(url=url, headers=headers, data=request_body)
                elif self._form_pattern.search(headers['Content-Type']):
                    request_body = {}
                    if body is not None:
                        request_body["jData"] = _json_dumps(body)
                    response = self.session.post(url=url, headers=headers, data=request_body)
                else:
                    msg = """In-Valid Content-Type in the Header Parameters"""
                    raise ApiException(status=0, reason=msg)
            elif method in ['GET']:
                if query_params:
                    url += '?' + urlencode(query_params)
                response = self.session.get(url=url, headers=headers)
            else:
                msg = """Cannot call the API with the provided HTTP Method"""
                raise ApiException(status=0, reason=msg)
        except Exception as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        # if not 200 <= response.status_code <= 299:
        #     raise ApiException(status=response.status_code, reason=response.reason, body=response.text)
        return response


