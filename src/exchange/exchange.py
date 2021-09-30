"""
交易所类，将下层交易所封装为对象，向上层提供接口
"""
from .test import test
from .config import Config
from importlib import import_module
from src.helpers import log


class exchange():
    def __init__(self, exchange_name):
        self.__init_exchange_module(exchange_name)

    def __init_exchange_module(self, exchange_name):
        """
        导入对应的交易所module，如果不存在于配置的交易所list中，则导入默认交易所huobi
        :param exchange_name: 交易所module名称
        :return: 交易所module
        """
        if exchange_name not in Config.EXCHANGE_LIST:
            log.e(f"unknown exchange name, using default exchange: {Config.DEFAULT_EXCHANGE}")
            exchange_name = Config.DEFAULT_EXCHANGE
        self.exchange_module = import_module(f".{exchange_name}", __package__)

    def test(self):
        test(self.exchange_module)
