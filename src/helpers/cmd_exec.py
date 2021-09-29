"""
执行系统命令
"""
import subprocess
import sys
from .log import log


def cmd_exec(cmd, env=None, log_file=None):
    """
    执行系统命令
    :param cmd: 要执行的命令，可以是str或者list
    :param env: 临时环境变量，默认None
    :param log_file: 重定向标准输出流和标准错误流到文件，默认None
    :return: 执行成功返回True，失败返回False
    :TODO: 运行超时处理机制
    """
    if type(cmd) == list:
        # 如果传入的命令是list，则拼接为str
        cmd = ' '.join(cmd)

    # 默认重定向
    stdout = sys.stdout
    stderr = sys.stderr
    if log_file is not None:
        # 指定输出文件时的重定向
        log_file_stream = open(log_file)
        stdout = log_file_stream
        stderr = log_file_stream

    log.i("Running command: " + cmd)
    if env is not None:
        log.i("with env: " + str(env))

    try:
        # 创建子进程
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=stderr, close_fds=True,
                             stdout=stdout, universal_newlines=True, shell=True, bufsize=1, env=env)
    except Exception as e:
        log.e("subprocess creation failed: ", e)
        return 1

    try:
        # 与子进程通信
        p.communicate()
    except Exception as e:
        log.e("subprocess failed: ", e)
        return False

    return p.returncode == 0
