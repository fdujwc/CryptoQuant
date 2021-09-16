from .security import Secret
from src.helpers.log import *


def test():
    log_i(Secret.READ_ACCESS)
    log_i(Secret.READ_SECRET)
    log_i(Secret.TRADE_ACCESS)
    log_i(Secret.TRADE_SECRET)
