"""
封装日志功能
"""
import time
INFO_MARKER = "I"
ERROR_MARKER = "E"
WARNING_MARKER = "W"


def log(marker, msg):
    """
    基础日志函数，所有日志函数都基于本函数
    :param marker: 标识日志类型的字符
    :param msg: 记录的信息
    :return:
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    format_s = "[{}][{}] ".format(marker, current_time)
    print(format_s + str(msg))


def log_i(msg):
    log(INFO_MARKER, msg)


def log_e(msg):
    log(ERROR_MARKER, msg)


def log_w(msg):
    log(WARNING_MARKER, msg)