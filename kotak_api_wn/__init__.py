# from __future__ import absolute_import

from kotak_api_wn.neo_utility import NeoUtility
from kotak_api_wn.exceptions import ApiTypeError
from kotak_api_wn.exceptions import ApiValueError
from kotak_api_wn.exceptions import ApiKeyError
from kotak_api_wn.exceptions import ApiAttributeError
from kotak_api_wn.exceptions import ApiException
from kotak_api_wn.req_data_validation import login_params_validation


from kotak_api_wn.api.login_api import LoginAPI
from kotak_api_wn.api.order_api import OrderAPI
from kotak_api_wn.api.order_history_api import OrderHistoryAPI
from kotak_api_wn.api.trade_report_api import TradeReportAPI
from kotak_api_wn.api.order_report_api import OrderReportAPI
from kotak_api_wn.api.modify_order_api import ModifyOrder
from kotak_api_wn.api.positions_api import PositionsAPI
from kotak_api_wn.api.portfolio_holdings_api import PortfolioAPI
from kotak_api_wn.api.margin_api import MarginAPI
from kotak_api_wn.api.scrip_master_api import ScripMasterAPI
from kotak_api_wn.api.limits_api import LimitsAPI
from kotak_api_wn.api.logout_api import LogoutAPI
from kotak_api_wn.settings import stock_key_mapping
from kotak_api_wn.NeoWebSocket import NeoWebSocket
from kotak_api_wn.HSWebSocketLib import HSWebSocket
from kotak_api_wn.HSWebSocketLib import HSIWebSocket
from kotak_api_wn.urls import WEBSOCKET_URL, PROD_BASE_URL, SESSION_PROD_BASE_URL, SESSION_UAT_BASE_URL, UAT_BASE_URL
from kotak_api_wn.neo_api import NeoAPI
from kotak_api_wn.api.scrip_search import ScripSearch
from kotak_api_wn import settings
from kotak_api_wn import req_data_validation

# Version
__version__ = "2.0.0"

# Module level imports for convenience
__all__ = [
    'NeoAPI',
    'NeoUtility',
    'LoginAPI',
    'OrderAPI',
    'OrderHistoryAPI',
    'TradeReportAPI',
    'OrderReportAPI',
    'ModifyOrder',
    'PositionsAPI',
    'PortfolioAPI',
    'MarginAPI',
    'ScripMasterAPI',
    'LimitsAPI',
    'LogoutAPI',
    'NeoWebSocket',
    'HSWebSocket',
    'HSIWebSocket',
    'ScripSearch',
    'ApiException',
    'ApiValueError',
    'ApiTypeError',
    'ApiKeyError',
    'ApiAttributeError',
    'settings',
    'req_data_validation',
]
