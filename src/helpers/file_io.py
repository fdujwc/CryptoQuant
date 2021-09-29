"""
提供写入文件的功能
"""
import os
from .log import log


def write_file(file_path, content, append=True, force=False):
    """
    写文件
    :param file_path: 文件绝对路径
    :param content: 写入的内容（字符串）
    :param append: 写入模式使用追加写入
    :param force: 是否强制写入
    :return:
    """
    write_mode = "a" if append else "w"
    if not append and os.path.exists(file_path):
        if force:
            # 强制写入模式：如果文件本来就存在，删除掉
            os.remove(file_path)
            log.w(f"original file deleted: {file_path}")
        else:
            log.e(f"file already exists: {file_path}")
    try:
        file_object = open(file_path, write_mode)
        file_object.write(content)
        file_object.close()
    except Exception as e:
        log.e("write file failed: ", e)