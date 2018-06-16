import multiprocessing
from time import sleep,ctime

class ClockProcess(multiprocessing.Process):
    def __init__(self,interval):
        super.__init__()
        self.interval = interval()

    def run(self):
        while True:
            print("Time:%s"% ctime())
            sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()

    while True:
        print("Sleeping...")
        sleep(1)