from multiprocessing import Process
import time


def run(num1, num2):
  print('子进程开启')
  print('子进程结果', num1 + num2)
  time.sleep(2)
  print('子进程结束')


if __name__ == '__main__':
  print('父进程开启')
  p = Process(target=run, name='process-test', args=(1, 2))
  p.start()
  # p.join()
  print('父进程结束')