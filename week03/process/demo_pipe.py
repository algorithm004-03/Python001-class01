from multiprocessing import Process, Pipe


def run(conn):
  conn.send('hello')
  conn.close()


if __name__ == '__main__':
  parent_conn, child_conn = Pipe(0)
  p = Process(target=run, args=(child_conn,))
  p.start()
  print(parent_conn.recv())
  p.join()