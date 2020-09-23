#coding:utf-8
from concurrent.futures import ThreadPoolExecutor
import requests
from time import sleep
import json
import pymysql
import collections
import matplotlib.pyplot as plt
# from pyecharts.charts import Pie

#解决中文显示问题
plt.rcParams['font.sans-serif'] = ['KaiTi']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def exec():
  items = (
      (city, page) for city in ('北京', '上海', '广州', '深圳') for page in range(1, 2))

  t = ThreadPoolExecutor(max_workers=4)
  result = list(t.map(execCrawi, items))
  # print(result)

  saveData(result)


def execCrawi(value):
  city, page = value

  headers = {
      'user-agent':
          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
      'accept':
          'application/json, text/javascript, */*; q=0.01',
      'accept-encoding':
          'gzip, deflate, br',
      'accept-language':
          'en-US,en;q=0.9',
      'content-type':
          'application/x-www-form-urlencoded; charset=UTF-8',
      'cookie':
          'JSESSIONID=ABAAABAABEIABCI733CCD198AD16F78B8F9639576A1A2C0; user_trace_token=20200715222414-376191c4-5e62-4eaf-ba57-4e5b0d6a07af; WEBTJ-ID=07152020%2C222415-17352dc9825198-0b56fcf658d5d3-4353760-1049088-17352dc9826692; PRE_UTM=; PRE_HOST=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5FPython%3Fpx%3Ddefault%26gx%3D%25E5%2585%25A8%25E8%2581%258C%26city%3D%25E5%258C%2597%25E4%25BA%25AC; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594823056; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217352dc9b8120e-02cda67258da29-4353760-1049088-17352dc9b82453%22%2C%22%24device_id%22%3A%2217352dc9b8120e-02cda67258da29-4353760-1049088-17352dc9b82453%22%7D; _ga=GA1.2.958843843.1594823056; _gat=1; _gid=GA1.2.147746628.1594823056; PRE_SITE=; LGUID=20200715222417-b748c765-c6ec-41ef-9e40-5bc669cacf6b; LGSID=20200715222417-43673683-8ed1-4f02-8278-54a23eb9790f; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=0b5a26a4c01d4252af3a72e068b05bd6; X_HTTP_TOKEN=2308a00f95efb6ef0603284951b3337b1053ffd22f; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1594823059; LGRID=20200715222420-f45f6521-8a5c-4572-ba6d-e4351b057d12',
      'referer':
          'https://www.lagou.com/jobs/list_python%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_2?px=default',
      'x-requested-with':
          'XMLHttpRequest'
  }
  url = f'https://www.lagou.com/jobs/positionAjax.json?px=new&gx=全职&city={city}&needAddtionalResult=false'
  data = {'first': 'false', 'pn': page, 'kd': 'Python'}

  sleep(5)
  return requests.post(url=url, data=data, headers=headers, verify=False).text


def saveData(data):
  items = convertData(data)
  saveDb(items)
  saveImg(items)


def convertData(data):
  items = []
  for s in data:
    v = json.loads(s)
    if ('success' in v) and v['success']:
      for item in v['content']['positionResult']['result']:
        items.append([
            item['city'], item['positionName'], item['salary'], item['workYear']
        ])
  return items


def saveDb(items):
  conn = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='nxx4545GGB46_fdg',
                         database='test',
                         charset='gb2312')
  qry = conn.cursor()
  try:
    # 执行批量插入
    qry.executemany(
        'insert into python_salary (city, name, salary, year) value (%s, %s, %s, %s)',
        items)
    conn.commit()
  except:
    conn.rollback()
  finally:
    qry.close()
    conn.close()


def saveImg(items):
  dic = collections.defaultdict(list)
  #解析薪资，取区间平均值
  for item in items:
    salary = item[2]
    salary = list(map(int, salary.replace('k', '000').split('-')))
    salary = sum(salary) / len(salary)
    dic[item[0]].append(salary)
  #画图1
  city, salarys = list(dic.keys()), list(dic.values())
  salarys = list(sum(salary) // len(salary) for salary in salarys)
  #饼图
  # plt.pie(salarys, labels=city, autopct='%1.1f%%', shadow=True, startangle=150)
  # plt.savefig('salary1.png')
  # plt.show()
  #柱状图
  plt.bar(city, salarys, color='rgbc')
  plt.savefig('salary.png')
  plt.show()
  #画图2
  # for key in dic:
  #   dic[key] = sum(dic[key]) / len(dic[key])
  # pie = Pie({'page_title': '北上广深最新python工作薪资'})
  # pie.add(series_name='薪资', data_pair=dic)
  # pie.render()


if __name__ == '__main__':
  exec()