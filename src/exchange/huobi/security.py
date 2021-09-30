"""
安全相关函数：请求签名，报文验签
"""
from .config import Secret
from src.helpers import hmac_sha256
from datetime import datetime


def sign_request(http_method, host, api, access_key, args=None):
    """
    对请求进行签名
    :param http_method: 请求方法：POST/GET，未来考虑兼容WebSocket
    :param host: api host域名地址
    :param api: api路由
    :param access_key: access key
    :param args: GET请求中可能有的更多参数
    :return: 返回可供requests库直接请求的附带签名的url
    """
    # request_str: 要被签名的字符串
    request_str = \
        f"{http_method}\n" + \
        f"{host}\n" + \
        f"{api}\n"
    # 基础请求参数
    request_args = {
        "accessKeyId": access_key,
        "signatureMethod": Secret.SIGN_METHOD,
        "signatureVersion": Secret.SIGN_VERSION,
        "timestamp": get_time_stamp()
    }
    # GET请求可能有的额外请求参数
    if args is not None:
        request_args.update(args)
    request_args_str = ""
    # 对所有请求参数进行排序拼接
    for key in sorted(request_args.keys()):
        request_args_str += f"{key}={request_args[key]}&"
    # 去掉末尾的&
    request_args_str = request_args_str[:-1]
    # 拼接形成最终的要被签名的字符串
    request_str += request_args_str
    # 签名
    signature = hmac_sha256(request_str, Secret.READ_SECRET)
    # 拼接附带签名的url
    signed_request_str = f"https://{host}{api}?{request_args_str}&signature={signature}"
    return signed_request_str


def get_time_stamp():
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
