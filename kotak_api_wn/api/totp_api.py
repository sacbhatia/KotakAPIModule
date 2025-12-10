from json import JSONDecodeError

from requests import session

from ..settings import PROD_URL


class TotpAPI(object):

    def __init__(self, api_client):
        self.api_client = api_client
        self.rest_client = api_client.rest_client
        self.totp_session = None

    def totp_login(self, mobile_number=None, ucc=None, totp=None):
        header_params = {'Authorization': self.api_client.configuration.consumer_key,
                         'neo-fin-key': self.api_client.configuration.get_neo_fin_key(),
                         'Content-Type': 'application/json'
                         }
        URL = self.api_client.configuration.get_domain(session_init=True) + '/' + PROD_URL.get('totp_login')
        body_params = {
            "mobileNumber": mobile_number,
            "ucc": ucc,
            "totp": totp
        }
        totp_login = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        try:
            totp_login_data = totp_login.json()
        except JSONDecodeError:
            return {
                "Error": "Unexpected response format. Expected JSON but received something else."
            }
        if 200 <= totp_login.status_code <= 299:
            self.api_client.configuration.view_token = totp_login_data.get("data").get("token")
            self.api_client.configuration.sid = totp_login_data.get("data").get("sid")
        return totp_login_data

    def totp_validate(self, mpin=None):
        header_params = {'Authorization': self.api_client.configuration.consumer_key,
                         "sid": self.api_client.configuration.sid,
                         "Auth": self.api_client.configuration.view_token,
                         'neo-fin-key': self.api_client.configuration.get_neo_fin_key()
                         }
        URL = self.api_client.configuration.get_domain(session_init=True) + '/' + PROD_URL.get('totp_validate')
        body_params = {
            "mpin": mpin
        }
        totp_validate = self.rest_client.request(
            url=URL, method='POST',
            headers=header_params,
            body=body_params
        )
        print(f"TOTP Validate URL: {URL}")
        print(f"TOTP Validate Status: {totp_validate.status_code}")
        print(f"TOTP Validate Response: {totp_validate.text}")
        try:
            totp_validate_data = totp_validate.json()
        except JSONDecodeError:
            return {
                "Error": "Unexpected response format. Expected JSON but received something else."
            }
        # totp_validate_data = totp_validate.json()
        if 200 <= totp_validate.status_code <= 299:
            print(f"TOTP Validate Data: {totp_validate_data}")
            # Try different response structures
            data = totp_validate_data.get("data") or totp_validate_data
            self.api_client.configuration.edit_token = data.get("token") or data.get("edit_token")
            self.api_client.configuration.edit_sid = data.get("sid") or data.get("edit_sid")
            self.api_client.configuration.edit_rid = data.get("rid") or data.get("edit_rid")
            self.api_client.configuration.serverId = data.get("hsServerId") or data.get("serverId")
            self.api_client.configuration.data_center = data.get("dataCenter")
            self.api_client.configuration.base_url = data.get("baseUrl")
            print(f"Set edit_token: {self.api_client.configuration.edit_token}")
            print(f"Set edit_sid: {self.api_client.configuration.edit_sid}")
            print(f"Full response: {totp_validate_data}")
        return totp_validate_data
