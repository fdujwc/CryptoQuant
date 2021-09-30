"""
Hashmac计算
"""
import hmac
from hashlib import sha256
from base64 import b64encode


def hmac_sha256(a_string, secret):
    key = secret.encode("utf-8")
    msg = a_string.encode("utf-8")
    signature = hmac.new(key, msg=msg, digestmod=sha256).digest()
    # 返回经过base64编码的签名
    return b64encode(signature).decode()
