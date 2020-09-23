from multiprocessing import Process, Queue


def run(q):
  q.put([11, 'test'])


if __name__ == '__main__':
  q = Queue()
  p = Process(target=run, args=(q,))
  p.start()
  print(q.get())
  p.join()