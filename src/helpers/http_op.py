"""
封装http方法
"""
from requests import get, post
from .log import log


def http_get(url, timeout=3):
    try:
        response = get(url=url, timeout=timeout)
    except:
        log.e("unable to send http request")
        return None
    status_code = response.status_code
    if status_code == 200:
        return response.text
    else:
        log.e(f"http request failed with code: {status_code}")
        log.e(response.request.url)
        return None


def http_post(url, data, timeout=3):
    try:
        response = post(url=url, data=data, timeout=timeout)
    except:
        log.e("unable to send http request")
        return None
    status_code = response.status_code
    if status_code == 200:
        return response.text
    else:
        log.e(f"http request failed with code: {status_code}")
        log.e(response.request.url)
        log.e(response.request.body)
    return None
