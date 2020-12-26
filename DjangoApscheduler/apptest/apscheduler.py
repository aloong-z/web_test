# !/usr/bin/env python
# coding: utf-8

import time


def update():
    local_time = time.localtime()
    local_time_str = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    print(local_time_str)


def show_love():
    print('I love qianqian', time.strftime("%H:%M:%S", time.localtime()))
