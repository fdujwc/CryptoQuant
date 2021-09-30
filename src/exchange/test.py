"""
exchange test
"""
from src.helpers import log


def test(exchange_module):
    log.i("exchange test")
    exchange_module.test()
