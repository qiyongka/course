# -*- coding: utf-8 -*-
import engine
import threading
import time

flag = 0
con = True
cond = threading.Condition()
cond2 = threading.RLock()
car = engine.Engine(11, 12, 13, 15, 16)


def run0():
    global con
    while 1:
        if cond.acquire():
            print("运动开始")
            while con:
                print(con)
                print("运动及避障")
                # 以下引用运动及避障代码
                car.start(90)
                if con == False:
                    break  # 说明：python的while循环无法实时退出，避免出问题需要适当确定con是否为False
            car.stop()  # 通信介入，车辆停止
            print(con)
            print("run0 jump")
            print(cond)
            cond.wait()
            print(cond)


def run1():
    global con, flag
    while 1:
        if cond2.acquire():
            time.sleep(5)
            flag = 1
            print("中断介入")
            # flag是中断标志位，当中断产生时flag置1
            if flag == 1:
                con = False
                print(con)
                print("run1")
                # 通讯处理代码段
                print("开始通信处理")
                time.sleep(3)
                print("通信处理完成")
                print(cond2)
                cond2.release()
                print(cond2)
                time.sleep(1)
            flag = 0


def run2():
    global con
    while 1:
        print(cond2)
        if cond2.acquire():
            print("规划介入")
            print(cond2)
            print(con)
            # 规划代码段
            print("开始规划处理")
            time.sleep(3)
            print("规划处理完成")
            con = True
            print(con)
            print("run2")
            if cond.acquire():
                cond.notify()
                print(cond)
                cond.release()
                print(cond)
            cond2.release()
            time.sleep(1)


if __name__ == '__main__':
    threading.Thread(target=run1).start()
    threading.Thread(target=run0).start()
    threading.Thread(target=run2).start()

    '''
    thread1 = MyThread(0, "main_thread").start()
    thread2 = MyThread(1, "communication").start()
    thread3 = MyThread(2, "find_road").start()
    '''
    '''
    class MyThread(threading.Thread):

        def __init__(self, threadID, name):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name

        def run(self):
            if self.threadID == 0:
                run0()
            elif self.threadID == 1:
                run1()
            elif self.threadID == 2:
                run2()
    '''
