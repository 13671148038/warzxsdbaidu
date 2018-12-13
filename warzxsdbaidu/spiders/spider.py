from scrapy.spiders import Spider
from scrapy import Request
import random
from warzxsdbaidu.items import WarzxsdbaiduItem
import time
import operator


class WarBaiduIsNo(Spider):
    name = 'wardemo'

    def __init__(self, *args, **kwargs):
        self.article = []
        self.word = []
        self.wordAttr = []
        self.articleCount = 0
        self.noArticleCount = 0
        self.wordCount = 0
        self.noWordCount = 0
        self.wordAttrCount = 0
        self.noWordAttrCount = 0
        self.cookies = {}
        self.headers = {}
        self.userAgents = []

    def start_requests(self):
        wordUrl = 'https://www.baidu.com/s?wd=http://m.2ge.cn/word/{0}'
        articleUrl = 'https://www.baidu.com/s?wd=http://m.2ge.cn/article/{0}/{1}/{2}'
        wordAttrUrl = 'https://www.baidu.com/s?wd=http://m.2ge.cn/word_attr/{0}/{1}/{2}'
        all = self.word + self.wordAttr + self.article
        for i in all:
            time.sleep(random.uniform(0, 1))
            self.headers['User-Agent'] = random.choices(self.userAgents)
            type = i[1]
            url = None
            if operator.eq('word', type):
                url = wordUrl.format(i[0])
            elif operator.eq("article", type):
                url = articleUrl.format(i[1], i[2], i[0])
            elif operator.eq('word_attr', type):
                url = wordAttrUrl.format(i[1], i[2], i[0])

            yield Request(url, callback=self.parse, headers=self.headers, cookies=self.cookies)

    def parse(self, response):
        body = response.xpath('//div[@id="content_left"]/div/h3/a/text()').extract()
        item = WarzxsdbaiduItem()
        url = response.url
        if len(body) > 0 and '二哥' in body[0]:
            item['body'] = body[0]
            if 'wdr' in url:
                self.wordAttrCount = self.wordAttrCount + 1
            elif 'ard' in url:
                self.articleCount = self.articleCount + 1
            else:
                self.wordCount = self.wordCount + 1
        else:
            item['path'] = url
            item['body'] = '无内容'
            if 'wdr' in url:
                self.noWordAttrCount = self.noWordAttrCount + 1
            elif 'ard' in url:
                self.noArticleCount = self.noArticleCount + 1
            else:
                self.noWordCount = self.noWordCount + 1
        yield item
