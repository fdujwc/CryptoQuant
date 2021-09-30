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

    def __run(self):
        print(2)
        log.i(f"[{self.name}] 开始运行")
        self.test_exchange.test()

    def __pause(self):
        log.i(f"[{self.name}] 暂停运行")

    def __wake(self):
        log.i(f"[{self.name}] 继续运行")

    def __exit(self):
        log.i(f"[{self.name}] 停止运行")
