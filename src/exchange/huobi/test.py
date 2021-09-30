"""
huobi test
"""
from .config import Secret
from src.helpers import log


def test():
    log.i("huobi test")
    log.i(Secret.READ_ACCESS)
    log.i(Secret.READ_SECRET)
    log.i(Secret.TRADE_ACCESS)
    log.i(Secret.TRADE_SECRET)
