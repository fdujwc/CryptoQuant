"""
USDT本位永续合约
"""
from .config import Secret, Config
from .security import sign_request
from src.helpers import http_get, http_post, log

api_dict = {
    "swap_account_info": "/linear-swap-api/v1/swap_account_info"
}
host = Config.HOST
access_key = Secret.READ_ACCESS
secret_key = Secret.READ_SECRET


def get_swap_account_info():
    api = api_dict["swap_account_info"]
    r = http_get(sign_request("GET", host, api, access_key))
    if r is not None:
        log.i(r)
