import requests
from lxml import etree
import datetime
import json

class NewsHeadlines():
    def __init__(self,hHot,hDate,hTitle,hId): 
        self.hHot = hHot
        self.hDate = hDate
        self.hTitle = hTitle
        self.hId = hId
    def get_news(self):
        return "- [" + self.hDate + "] " + self.hId + "." + self.hTitle + " 热度：" + self.hHot

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Cookie': '''SUB=_2AkMV4ianf8NxqwJRmP4QyW3ma45zyw_EieKjvtd8JRMxHRl-yT9kqkgStRB6PmIISKq4w7FMaKk5oxKZ4HPK02FGFnro; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh.omr7J4MDnPrsemO5SxI9; SINAGLOBAL=1194640036816.379.1656662419127; UOR=localhost:8080,s.weibo.com,124.222.34.234; _s_tentry=-; Apache=6311321839856.308.1659449372617; ULV=1659449372676:5:1:2:6311321839856.308.1659449372617:1659251729239'''
}

needNews = []
newsList = []

def get_hot_list(url,the_day):
    '''
    微博热搜页面采集，获取详情页链接后，跳转进入详情页采集
    :param url: 微博热搜页链接
    :return: None
    '''
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    tr_list = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr')
    count = 0
    for tr in tr_list:
        title = tr.xpath('./td[2]/a/text()')[0]
        try:
            rank = tr.xpath('./td[1]/text()')[0]
            hot = tr.xpath('./td[2]/span/text()')[0]
        except Exception:
            rank = '置顶'
            hot = '置顶'
        if '•' == rank:
            continue
        news_headlines = NewsHeadlines(hot,the_day,title,rank)
        needNews.append(news_headlines.__dict__)
        newsList.append(news_headlines)

if __name__ == '__main__':
    ISOTIMEFORMAT = '%Y-%m-%d'
    the_day = datetime.datetime.now().strftime(ISOTIMEFORMAT)
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    get_hot_list(url,the_day)
    jsonlist = json.dumps(needNews, ensure_ascii=False)
    print(jsonlist)
    news_count = 0
    news_text = ""
    for news in newsList:
        if news_count > 0 and news_count < 6 :
            news_text += news.get_news() + "\n"
        news_count += 1
    with open("./spider/wbtext.md", "r+") as f:
        old = f.read()
        f.seek(0)
        f.write("### 微博热搜记录更新 -5条\n")
        f.write(news_text)
        f.write(old)

