from multiprocessing.pool import Pool
from time import sleep


def run(x):
  return x * x


if __name__ == '__main__':
  with Pool(processes=4) as p:
    result = p.apply_async(run, (9,))
    print(result.get(timeout=1))

    result = p.apply_async(sleep, (10,))
    # print(result.get(timeout=15))
    print(result.get(timeout=9))