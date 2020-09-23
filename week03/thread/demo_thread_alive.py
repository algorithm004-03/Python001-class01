from threading import Thread
from time import sleep


def run():
  sleep(5)


t1 = Thread(target=run)
print(t1.is_alive())

t1.start()

print(t1.getName())
print(t1.is_alive())

t1.join()

print(t1.is_alive())