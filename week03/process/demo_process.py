from multiprocessing import Process
import os


def execAdd(num1, num2):
  print('process id:', os.getpid())
  return num1 + num2


if __name__ == '__main__':
  p = Process(target=execAdd, name='process-demo', args=(3, 5))
  p.start()
  p.join()
  print('process id:', os.getpid())