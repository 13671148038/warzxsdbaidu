# -*- coding: utf-8 -*-

# Scrapy settings for warzxsdbaidu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'warzxsdbaidu'

SPIDER_MODULES = ['warzxsdbaidu.spiders']
NEWSPIDER_MODULE = 'warzxsdbaidu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'warzxsdbaidu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
}
USER_AGENTS = [
            'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        ]

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'warzxsdbaidu.middlewares.WarzxsdbaiduSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'warzxsdbaidu.middlewares.WarzxsdbaiduDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'warzxsdbaidu.pipelines.WarzxsdbaiduPipeline': 300,
#}
ITEM_PIPELINES = {
   'warzxsdbaidu.pipelines.WarzxsdbaiduPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MYSQL_HOST = '101.36.144.167'
MYSQL_DBNAME = 'zxcms'
MYSQL_USER = 'zx114'
MYSQL_PASSWD = '20161021'
# LOG_FILE = "/usr/local/lib/python3.5/site-packages/scrapyd/dbs/logs/zxsdisno/demo/mySpider.log"
# LOG_FILE = r"C:\Users\13671\Desktop\mySpider.log"
LOG_LEVEL = "DEBUG"

COOKIES = {
            'BD_UPN	': '13314752',
            'BAIDUID': '8A280E2849B24A71325777A587EC0D2A:FG=1',
            'BIDUPSID': '8A280E2849B24A71325777A587EC0D2A',
            'PSTM': '1540197775',
            'BDUSS': 'HNiSEVTQlV3U3V5SVJ6Rnd5Z2hZZFZnZUxPbGVwN1ViMn5RTVNJWHl6RnJ6VFZjQUFBQUFBJCQAAAAAAAAAAAEAAACRUkyFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGtADlxrQA5cR',
            'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
            'BD_CK_SAM': '1',
            'H_PS_645EC': 'a680OoHHIbTSnh/luMiDlQaiV8ocIgy+LqpZIwaojh+a6IHHjaHmIiIs2KM',
            'H_PS_PSSID': '1436_21098_28019_27244_22074',
            'PSINO': '2',
            'sugstore': '0',
        }
