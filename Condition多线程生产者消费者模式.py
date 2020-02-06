#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    : 2/6/2020 7:09 PM
@Author  : Alfred Lam
@FileName: Condition多线程生产者消费者模式.py
@Software: PyCharm
"""
import threading
import random
gMoney = 0
gCondition = threading.Condition()
gTimes = 0


class Producer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            earn_money = random.randint(0, 100)
            gCondition.acquire()
            if gTimes >= 100:
                gCondition.release()
                break
            gMoney += earn_money
            gTimes += 1     # 注意，gTimes要放到这里来加，因为最开始的值是0，如果在gMoney之前加的话，当gTimes加到10时，只循环了9次
            print("%s生产了%d元" % (threading.current_thread().name, earn_money))
            gCondition.notify_all()
            gCondition.release()


class Consumer(threading.Thread):
    def run(self) -> None:
        global gMoney
        global gTimes
        while True:
            spend_money = random.randint(0, 100)
            gCondition.acquire()
            while gMoney < spend_money:
                if gTimes >= 100:
                    print("%s想消费%d元，但是钱不够，并且生产者已经停止生产了！" % (threading.current_thread().name, spend_money))
                    gCondition.release()
                    return
                print("%s想消费%d元，但是钱不够，正在等待生产者生产。" % (threading.current_thread().name, spend_money))
                gCondition.wait()
            gMoney -= spend_money
            print("%s消费了%d元，余额为%d" % (threading.current_thread().name, spend_money, gMoney))
            gCondition.release()


def main():
    for i in range(1, 3):
        th = Producer(name="生产者%d号" % i)
        th.start()
    for x in range(1, 6):
        th = Consumer(name="消费者%d号" % x)
        th.start()


if __name__ == '__main__':
    main()
