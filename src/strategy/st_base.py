"""
基础策略，所有策略都继承自此策略
"""
from src.helpers import log


class st_base():
    def __init__(self):
        self.name = "基础策略"
        self.__set_status("READY")

    def run(self):
        """
        接口run，运行策略
        :return:
        """
        self.__set_status("RUNNING")
        self.__run()

    def pause(self):
        """
        接口pause，暂停策略
        :return:
        """
        self.__set_status("PAUSED")
        self.__pause()

    def wake(self):
        """
        接口wake，唤醒策略
        :return:
        """
        self.__set_status("RUNNING")
        self.__wake()

    def exit(self):
        """
        接口exit，结束策略
        :return:
        """
        self.__set_status("EXITED")
        self.__exit()

    def __run(self):
        log.i(f"[{self.name}] 开始运行")

    def __pause(self):
        log.i(f"[{self.name}] 暂停运行")

    def __wake(self):
        log.i(f"[{self.name}] 继续运行")

    def __exit(self):
        log.i(f"[{self.name}] 停止运行")

    def __set_status(self, status_code):
        if status_code == "READY":
            self.status = 1
        elif status_code == "RUNNING":
            self.status = 2
        elif status_code == "PAUSED":
            self.status = 3
        elif status_code == "EXITED":
            self.status = 4
        else:
            log_e("unknown status code")
