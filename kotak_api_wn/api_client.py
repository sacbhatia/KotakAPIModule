from __future__ import absolute_import
from . import rest


class ApiClient(object):
    """
    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    param header_value: a header value to pass when making calls to
        the API.
    """
    __slots__ = ('configuration', 'rest_client', 'default_headers', '_user_agent')

    def __init__(self, configuration, header_name=None, header_value=None):
        self.configuration = configuration
        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = {}
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self._user_agent = 'NeoTradeApi-python/1.0.0/python'

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        self._user_agent = value
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value