"""
测试策略
"""
from .st_base import st_base
from src.helpers import log
from src.exchange import exchange


class st_test(st_base):
    def __init__(self):
        super().__init__()
        self.name = "测试策略"
        self.test_exchange = exchange("huobi")

    def run(self):
        super().run()
        self.test_exchange.test()

    def pause(self):
        super().pause()

    def wake(self):
        super().wake()

    def exit(self):
        super().exit()
