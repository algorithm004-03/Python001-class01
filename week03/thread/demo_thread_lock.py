from threading import Thread, Lock
from time import sleep

num = 0
mutex = Lock()


class DemoThread(Thread):

  def run(self):
    global num
    if mutex.acquire():
      num += 1
      sleep(1)
      print(f'{self.name}: num value is {num}')
    mutex.release()


if __name__ == '__main__':
  for _ in range(5):
    t = DemoThread()
    t.start()