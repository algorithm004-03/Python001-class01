import multiprocessing
import os
import time


def debug_info(title):
  print('*' * 20)
  print(title)
  print('模块名称:', __name__)
  print('父进程:', os.getppid())
  print('子进程:', os.getpid())
  print('*' * 20)


def run1(name):
  # print('hello', name)
  debug_info(name)


if __name__ == '__main__':
  run1('main')
  p = multiprocessing.Process(target=run1, args=('sub',))
  p.start()
  for s in multiprocessing.active_children():
    print(f'子进程名称: {s.name}  id: { str(s.pid) }')
  print('进程结束')
  print(f'CPU核心数量: { str(multiprocessing.cpu_count()) }')
  p.join()