from multiprocessing import Process
import os
import time


class DefProcess(Process):

  def __init__(self, num):
    super().__init__()
    self.num = num

  #重写run方法
  def run(self):
    while True:
      print(f'我是进程：{self.num}，我的pid是：{os.getpid()}')
      time.sleep(1)


if __name__ == '__main__':
  for i in range(2):
    # 当不给Process指定target时，会默认调用Process类里的run()方法
    DefProcess(i).start()