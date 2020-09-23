from multiprocessing import Process, Value, Lock
from time import sleep


def job(l, v, n):
  l.acquire()
  for _ in range(5):
    sleep(0.1)
    v.value += n
    print(v.value, end="|")
  l.release()


if __name__ == '__main__':
  l = Lock()
  v = Value('i', 0)
  p1 = Process(target=job, args=(l, v, 1))
  p2 = Process(target=job, args=(l, v, 3))
  p1.start()
  p2.start()
  p1.join()
  p2.join()