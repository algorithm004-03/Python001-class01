from multiprocessing.pool import Pool
from time import sleep, time
import random
from os import getpid


def run(name):
  print(f'{name}子进程开始，进程ID：{getpid()}')
  start = time()
  sleep(random.choice([1, 2, 3, 4]))
  end = time()
  print(f'{name}子进程结束，进程ID：{getpid()}。耗时{end - start}')


if __name__ == '__main__':
  p = Pool(processes=4)
  for i in range(10):
    p.apply_async(run, args=(i,))
  p.close()
  # p.terminate()
  p.join()