from threading import Thread
from time import sleep

num = 0


def addone():
  global num
  num += 1
  sleep(1)
  print(f'num value is {num}\n')


if __name__ == '__main__':
  for i in range(10):
    t = Thread(target=addone)
    t.start()