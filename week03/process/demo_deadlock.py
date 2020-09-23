from multiprocessing import Process, Queue


def run(q):
  q.put('ha ' * 10)


if __name__ == '__main__':
  q = Queue()
  p = Process(target=run, args=(q,))
  p.start()
  # p.join()
  obj = q.get()
  print(obj)
  p.join()