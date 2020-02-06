#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2/6/2020 7:09 PM
@Author  : Alfred Lam
@FileName: Lock多线程生产者消费者模式.py
@Software: PyCharm
"""
import threading
import random
gMoney = 0
gLock = threading.Lock()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            earn_money = random.randint(0, 100)
            gLock.acquire()
            if gTimes >= 10:
                gLock.release()
                break
            gMoney += earn_money
            gTimes += 1     # 注意，gTimes要放到这里来加，因为最开始的值是0，如果在gMoney之前加的话，当gTimes加到10时，只循环了9次
            print("%s生产了%d元" % (threading.current_thread().name, earn_money))
            gLock.release()


class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            spend_money = random.randint(0, 100)
            gLock.acquire()
            if gMoney >= spend_money:
                gMoney -= spend_money
                print("%s花费了%d元，目前余额还有%d元" % (threading.current_thread().name, spend_money, gMoney))
            else:
                if gTimes >= 10:
                    gLock.release()
                    break
                print("%s想消费%d元但是余额不足，余额只有%d元" % (threading.current_thread().name, spend_money, gMoney))
            gLock.release()


def main():
    for i in range(1, 6):
        th = Producer(name="生产者%d号" % i)
        th.start()
    for x in range(1, 6):
        th = Consumer(name="消费者%d号" % x)
        th.start()


if __name__ == '__main__':
    main()