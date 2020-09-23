from threading import Thread, Lock, Condition
from queue import Queue
from time import sleep
import random

writelock = Lock()


class Producer(Thread):

  def __init__(self, q, con, name):
    super().__init__()
    self.q = q
    self.con = con
    self.name = name

  def run(self):
    while True:
      global writelock
      self.con.acquire()

      if self.q.full():
        with writelock:
          print('Queue is full , producer wait')
        self.con.wait()
      else:
        value = random.randint(0, 10)
        with writelock:
          print(f'{self.name} put value {self.name} {str(value)} in queue')
        self.q.put((f'{self.name} : {str(value)}'))
        self.con.notify()
        sleep(1)
    self.con.release()


class Consumer(Thread):

  def __init__(self, q, con, name):
    super().__init__()
    self.q = q
    self.con = con
    self.name = name

  def run(self):
    while True:
      global writelock
      self.con.acquire()

      if self.q.empty():
        with writelock:
          print('Queue is empty , consumer wait')
        self.con.wait()
      else:
        value = self.q.get()
        with writelock:
          print(f'{self.name} get value {value} from queue')
        self.con.notify()
        sleep(1)
    self.con.release()


if __name__ == '__main__':
  q = Queue(5)
  con = Condition()

  p1 = Producer(q, con, 'p1')
  p1.start()
  p2 = Producer(q, con, 'p2')
  p2.start()

  c1 = Consumer(q, con, 'c1')
  c1.start()