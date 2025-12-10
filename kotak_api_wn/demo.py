# from .neo_api import NeoAPI
import io
from .neo_api import NeoAPI
import threading


def on_message(message):
    print('[Res]: ', message)


def on_error(message):
    result = message
    print('[OnError]: ', result)


# Example usage - Replace with your actual credentials
client = NeoAPI(consumer_key="YOUR_CONSUMER_KEY",
                               environment='prod',
                               on_message=on_message,
                               on_error=on_error)

# For TOTP authentication (recommended):
client = NeoAPI(consumer_key="YOUR_CONSUMER_KEY", environment='prod')
totp_response = client.totp_login(mobile_number="YOUR_MOBILE", ucc="YOUR_UCC", totp="123456")
client.totp_validate(mpin="YOUR_MPIN")

# Legacy broker login (deprecated):
# client.login(mobilenumber="YOUR_MOBILE", password="YOUR_PASSWORD")
# client.session_2fa("YOUR_OTP")

# Example API calls
print(client.search_scrip(exchange_segment="nse_fo", symbol="BANKNIFTY", expiry="", option_type="CE",strike_price="45000"))
client.subscribe_to_orderfeed()
