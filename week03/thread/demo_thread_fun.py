from threading import Thread


def run(n):
  print(f'current task: {n}\n')


if __name__ == '__main__':
  t1 = Thread(target=run, args=('thread 1',))
  t2 = Thread(target=run, args=('thread 2',))
  t1.start()
  t2.start()