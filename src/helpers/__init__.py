"""
基础工具package，封装与操作系统和网络的交互，提供日志，加解密，签名验证等常用功能
"""
from .log import log
from .hashmac import calc_hashmac