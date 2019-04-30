import time


def getTime():
    '''
    获取当前时间
    :return: 当前时间，格式%H:%M:%S
    '''
    now = time.strftime('%H:%M:%S', time.localtime(time.time()))

    return now


def getDate():
    '''
    获取当前日期
    :return: 当前日期，格式%m%d
    '''
    now = time.strftime('%m%d', time.localtime(time.time()))

    return now
