from multiprocessing import Process, Value
from time import sleep


def job(v, n):
  for _ in range(5):
    sleep(0.1)
    v.value += n
    print(v.value, end="|")


if __name__ == '__main__':
  v = Value('i', 0)
  p1 = Process(target=job, args=(v, 1))
  p2 = Process(target=job, args=(v, 3))
  p1.start()
  p2.start()
  p1.join()
  p2.join()