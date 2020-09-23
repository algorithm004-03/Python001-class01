import requests
from lxml import etree
import pymysql
import codecs


def main():
    save_data(parse_data(get_data()))


def get_data():
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    #没有豆瓣账号，请求返回utf-8乱码
    # url = f'https://movie.douban.com/subject/30170546/comments?start=&limit=20&sort=new_score&status=P'
    url = f'http://movie.mtime.com/259167/reviews/short/new.html'
    return requests.get(url=url, headers=headers, verify=False).text


def parse_data(data):
    items = []
    selector = etree.HTML(data)
    for info in selector.xpath(
            '//div[@class="db_shortcomment db_shortcomlist new_shortcomlist"]/dl/dd'
    ):
        short = info.xpath('div/h3/text()')[0]
        score = info.xpath(
            'div/div[@class="comboxuser"]/div/p[2]/span/text()')[0].strip()

        items.append((short, score))
    return items


def save_data(data):
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='nxx4545GGB46_fdg',
                           database='test',
                           charset='utf8mb4')
    qry = conn.cursor()
    try:
        # 执行批量插入
        qry.executemany('insert into movie_short (short, score) value (%s, %s)',
                        data)
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        qry.close()
        conn.close()


if __name__ == '__main__':
    main()
