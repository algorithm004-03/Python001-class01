from multiprocessing import Pool
import time


def run(x):
  return x * x


if __name__ == '__main__':
  with Pool(processes=4) as p:
    print(p.map(run, range(10)))

    im = p.imap(run, range(10))
    print(im)
    print(next(im))
    print(next(im))
    print(im.next())