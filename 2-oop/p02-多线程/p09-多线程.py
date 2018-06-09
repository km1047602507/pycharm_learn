'''
利用time生成两个函数
顺序调用
计算总的运行时间
'''
import time
import _thread as thread
def loop1():
    print('Start loop1 at:',time.ctime())
    time.sleep(4)
    print('End loop1 at:',time.ctime())

import time
def loop2():
    print('Start loop2 at:',time.ctime())
    time.sleep(2)
    print('End loop2 at:',time.ctime())


def main():
    print('Starting at:',time.ctime())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    print('Ending at:',time.ctime())

if __name__ == '__main__':
    main()

