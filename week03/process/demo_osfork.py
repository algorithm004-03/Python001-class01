import os

# os.fork()
# print('111')

if os.fork() == 0:
  print(f'我是子进程,我的pid是:{os.getpid()}我的父进程id是:{os.getppid()}')
else:
  print(f'我是父进程,我的pid是: {os.getpid()}')