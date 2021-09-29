"""
封装日志功能
"""
import time


class log_class:
    def __init__(self):
        self.INFO_MARKER = "I"
        self.ERROR_MARKER = "E"
        self.WARNING_MARKER = "W"

    def __log(self, marker, msg):
        """
        基础日志函数，所有日志函数都基于本函数
        :param marker: 标识日志类型的字符
        :param msg: 记录的信息
        :return:
        """
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        format_s = f"[{marker}][{current_time}] "
        print(format_s + str(msg))

    def i(self, msg):
        self.__log(self.INFO_MARKER, msg)

    def e(self, msg, exception):
        msg = f"{msg}: {str(exception)}"
        self.__log(self.ERROR_MARKER, msg)

    def w(self, msg):
        self.__log(self.WARNING_MARKER, msg)


log = log_class()
