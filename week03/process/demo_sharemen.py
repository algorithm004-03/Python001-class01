from multiprocessing import Process, Value, Array


def run(num, arr):
  num.value = 3.14
  for i in arr:
    arr[i] = -arr[i]


if __name__ == '__main__':
  num = Value('d', 0.0)
  arr = Array('i', range(10))

  p = Process(target=run, args=(
      num,
      arr,
  ))
  p.start()
  p.join()

  print(num.value)
  print(arr[:])