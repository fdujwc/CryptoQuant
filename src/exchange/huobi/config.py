"""
火币交易所相关配置
"""
from os import environ


class Secret(object):
    try:
        # 读取操作access key，用于发送读取请求
        READ_ACCESS = environ["READ_ACCESS"]
        # 读取操作secret，用于验证交易所返回报文的签名
        READ_SECRET = environ["READ_SECRET"]
        # 交易操作access key，用于发送交易请求
        TRADE_ACCESS = environ["TRADE_ACCESS"]
        # 交易操作secret，用于验证交易所返回报文的签名
        TRADE_SECRET = environ["TRADE_SECRET"]
    except:
        READ_ACCESS = 'environ["READ_ACCESS"]'
        READ_SECRET = 'environ["READ_SECRET"]'
        TRADE_ACCESS = 'environ["TRADE_ACCESS"]'
        TRADE_SECRET = 'environ["TRADE_SECRET"]'
    # 签名算法
    SIGN_METHOD = "HmacSHA256"
    # 签名算法版本
    SIGN_VERSION = 2


class Config(object):
    # api服务器
    HOST = "api.hbdm.com"
