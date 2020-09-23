from threading import Thread


class DemoThread(Thread):

  def __init__(self, name):
    super().__init__()
    self.name = name

  def run(self):
    print(f'current task: {self.name}')


if __name__ == '__main__':
  t1 = DemoThread('thread 1')
  t2 = DemoThread('thread 2')
  t1.start()
  t2.start()
  t1.join()
  t2.join()