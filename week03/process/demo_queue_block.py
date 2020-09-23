from multiprocessing import Process, Queue
from time import sleep
from os import getpid


def runWrite(q):
  print(f"启动Write子进程：{getpid()}")
  for c in ['T', 'E', 'S', 'X']:
    q.put(c)
    sleep(1)
  print(f"结束Write子进程：{getpid()}")


def runRead(q):
  print(f"启动Read子进程：{getpid()}")
  while True:
    print(q.get())
  print(f"结束Read子进程：{getpid()}")


if __name__ == '__main__':
  q = Queue(maxsize=24)
  pw = Process(target=runWrite, args=(q,))
  pr = Process(target=runRead, args=(q,))
  pw.start()
  pr.start()
  pw.join()
  pr.terminate()
