# from multiprocessing import Pool, Queue
from concurrent.futures import ProcessPoolExecutor, process
from multiprocessing import cpu_count
from argparse import ArgumentParser
import os
import socket
import collections
import json


def execCmd(args):
  ips = getIp(args.ip)
  if not ips:
    return

  # 在进程池使用queue报错了
  # q1 = Queue()
  # for ip in ips:
  #   for port in range(1, 1025):
  #     q1.put((ip, port))
  result = []

  if args.fun == 'ping':
    p = ProcessPoolExecutor(max_workers=args.num)
    result = list(p.map(pingExec, ips))
    # p.shutdown(wait=True)
    # print(result)
    # print('succ: ', list(row[0] for row in result if row[1]))
    # print('fail: ', list(row[0] for row in result if not row[1]))
  elif args.fun == 'tcp':
    task = ((ip, port) for ip in ips for port in range(22, 33))
    p = ProcessPoolExecutor(max_workers=args.num)
    result = list(p.map(tcpExec, task))
  else:
    print('-f opt must is ping or tcp!')
    return

  saveExec(args.save, result)


def parseOpt():
  parser = ArgumentParser()
  parser.add_argument('-n', '--num', default=cpu_count())
  parser.add_argument('-f', '--fun', default='ping')
  parser.add_argument('-ip', '--ip')
  parser.add_argument('-w', '--save')
  return parser.parse_args()


def getIp(ip):
  ips = []
  if ip:
    tmp = ip.split('-')
    if len(tmp) == 1:
      ips.append(ip)
    elif len(tmp) == 2:
      host = '.'.join(tmp[0].split('.')[:-1])
      begin = int(tmp[0].split('.')[3])
      end = int(tmp[1].split('.')[3]) + 1
      for i in range(begin, end):
        ips.append(host + '.' + str(i))
  return ips


def pingExec(ip):
  cmd = f'ping -c 1 {ip}'
  # print(cmd)
  rep = os.popen(cmd).read()
  # print(rep)
  return [rep.lower().count('ttl') > 0, ip]


def tcpExec(value):
  ip, port = value
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = [False, ip, port]
  try:
    server.connect((ip, port))
    # print(f'{ip} port {port} is open')
    result = [True, ip, port]
  except Exception as err:
    pass
    # print(f'{ip} port {port} is close {err}')
  finally:
    server.close()
  return result


def saveExec(filename, result):
  if filename:
    # ans = {'succ': [], 'fail': []}
    ans = collections.defaultdict(list)
    for row in result:
      if row[0]:
        # ans.
        ans['succ'].append(row[1:])
      else:
        ans['fail'].append(row[1:])
    with open(filename, 'w') as f:
      json.dump(ans, f)


if __name__ == '__main__':
  execCmd(parseOpt())
