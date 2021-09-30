"""
基础策略，所有策略都继承自此策略
"""
from src.helpers import log
from .config import Config


class st_base():
    def __init__(self):
        self.name = "基础策略"
        self.__set_status(Config.ST_STATUS.READY)

    def run(self):
        """
        接口run，运行策略
        :return:
        """
        self.__set_status(Config.ST_STATUS.RUNNING)
        log.i(f"[{self.name}] 开始运行")

    def pause(self):
        """
        接口pause，暂停策略
        :return:
        """
        self.__set_status(Config.ST_STATUS.PAUSED)
        log.i(f"[{self.name}] 暂停运行")

    def wake(self):
        """
        接口wake，唤醒策略
        :return:
        """
        self.__set_status(Config.ST_STATUS.RUNNING)
        log.i(f"[{self.name}] 继续运行")

    def exit(self):
        """
        接口exit，结束策略
        :return:
        """
        self.__set_status(Config.ST_STATUS.EXITED)
        log.i(f"[{self.name}] 停止运行")

    def __set_status(self, status_code):
        self.status = status_code
