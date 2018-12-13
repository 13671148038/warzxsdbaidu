# -*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class WarzxsdbaiduPipeline(object):

    def __init__(self, *args, **kwargs):
        db = pymysql.connect(host=kwargs['db_url'], db=kwargs['db_name'], user=kwargs['db_user_name'],
                             password=kwargs['db_password'])
        self.cursor = db.cursor()
        self.wordF = None
        self.wordAttrF = None
        self.articleF = None
        self.cookies = kwargs["cookies"]
        self.user_agents = kwargs["user_agents"]
        self.headers = kwargs["headers"]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_url=crawler.settings.get('MYSQL_HOST'),
            db_name=crawler.settings.get('MYSQL_DBNAME'),
            db_user_name=crawler.settings.get('MYSQL_USER'),
            db_password=crawler.settings.get('MYSQL_PASSWD'),
            cookies=crawler.settings.get('COOKIES'),
            headers=crawler.settings.get('DEFAULT_REQUEST_HEADERS'),
            user_agents=crawler.settings.get('USER_AGENTS'),
        )

    def open_spider(self, spider):
        spider.cookies = self.cookies
        spider.headers = self.headers
        spider.userAgents = self.user_agents

        # 获取文章
        sql = 'select article_id, \'article\' from tb_article where status=3 and is_publish = 0 and attr = 1 limit 0,20'
        self.cursor.execute(sql),
        results = self.cursor.fetchall()
        spider.article = results

        # 获取聚合词条    warb端是goodclassid
        sql = 'select goods_class_id, \'word\' from tb_word where status=3 and is_publish = 0 limit 0,20'
        self.cursor.execute(sql),
        results = self.cursor.fetchall()
        spider.word = results

        # 获取词条        war端是频道加栏目加id加/1
        sql = (
            'select word_attr_code ,\'word_attr\' '
            'from tb_word word left join tb_word_attr wordAttr on word.word_id = wordAttr.word_id '
            'where word.status=3 and word.is_publish = 0 limit 0,20'
        )
        self.cursor.execute(sql),
        results = self.cursor.fetchall()
        spider.wordAttr = results

        self.wordF = open(r'C:\Users\13671\Desktop\war\word.txt', 'w')
        self.wordAttrF = open(r'C:\Users\13671\Desktop\war\wordAttr.txt', 'w')
        self.articleF = open(r'C:\Users\13671\Desktop\war\article.txt', 'w')
        # self.wordF = open(r'/usr/local/lib/python3.5/site-packages/scrapyd/dbs/logs/zxsdisno/demo/word.txt', 'w')
        # self.wordAttrF = open(r'/usr/local/lib/python3.5/site-packages/scrapyd/dbs/logs/zxsdisno/demo/wordAttr.txt', 'w')
        # self.articleF = open(r'/usr/local/lib/python3.5/site-packages/scrapyd/dbs/logs/zxsdisno/demo/article.txt', 'w')

    def process_item(self, item, spider):
        if '无内容' in item['body']:
            path = item["path"]
            if 'wdr' in path:
                self.wordAttrF.write('{0}==={1}'.format(item["body"], item["path"]))
                self.wordAttrF.write("\n")
            elif 'ard' in path:
                self.articleF.write('{0}==={1}'.format(item["body"], item["path"]))
                self.articleF.write("\n")
            else:
                self.wordF.write('{0}==={1}'.format(item["body"], item["path"]))
                self.wordF.write("\n")
        return item

    def close_spider(self, spider):
        self.wordF.write('count:{0}   '.format(spider.wordCount))
        self.wordF.write('nocount;{0}   '.format(spider.noWordCount))
        self.wordF.write('allcount;{0}'.format(len(spider.word)))
        self.wordF.write("\n")

        self.wordAttrF.write('count:{0}   '.format(spider.wordAttrCount))
        self.wordAttrF.write('nocount;{0}   '.format(spider.noWordAttrCount))
        self.wordAttrF.write('allcount;{0}'.format(len(spider.wordAttr)))
        self.wordAttrF.write("\n")

        self.articleF.write('count:{0}   '.format(spider.articleCount))
        self.articleF.write('nocount;{0}   '.format(spider.noArticleCount))
        self.articleF.write('allcount;{0}'.format(len(spider.article)))
        self.articleF.write("\n")

        self.wordF.close()
        self.wordAttrF.close()
        self.articleF.close()
        self.cursor.close()
