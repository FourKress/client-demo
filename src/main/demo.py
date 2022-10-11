# -*- coding: utf-8 -*-
from threading import Timer
import time
import sys

print("进程 " +sys.argv[1] +" 执行。")

count = 1

def print_count():
    global t, count
    print("当前执行次数：%s" % count)
    count += 1
    if count < 4:
        print("循环执行py脚本")
        t = Timer(1, print_count)
        t.start()

t = Timer(3, print_count)

t.start()


