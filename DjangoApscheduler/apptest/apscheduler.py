# !/usr/bin/env python
# coding: utf-8

import logging
import time


def update():
    local_time = time.localtime()
    local_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    log = logging.getLogger(' __LINE__ ')
    log.info(local_time_str)


def show_love():
    log = logging.getLogger(' __LINE__ ')
    log.info('I love you {}'.format(time.strftime("%H:%M:%S", time.localtime())))
