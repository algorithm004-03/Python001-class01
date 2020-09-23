from twisted.web.client import getPage
from twisted.internet import defer
from twisted.internet import reactor


def callback1(*args):
  print('执行回调1：', args)


def callback2(*args, **kwargs):
  print('执行回调2：', args, kwargs)


@defer.inlineCallbacks
def start(url):
  d = getPage(url.encode('utf-8'))
  d.addCallback(callback1)
  d.addCallback(callback2)
  yield d


def stop(*args, **kwargs):
  reactor.stop()


li = []
for url in ['http://www.baidu.com', 'http://www.sougou.com']:
  li.append(start(url))
print(li)

d = defer.Deferred(li)
d.addBoth(stop)
reactor.run()