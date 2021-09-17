from .security import Secret
from src.helpers import log_i


def test():
    log_i(Secret.READ_ACCESS)
    log_i(Secret.READ_SECRET)
    log_i(Secret.TRADE_ACCESS)
    log_i(Secret.TRADE_SECRET)
