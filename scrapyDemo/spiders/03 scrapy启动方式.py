# 通过下面的方式可以启动爬虫 也可以在命令行中输入scrapy crawl 爬虫名 来启动爬虫；

from scrapy.cmdline import execute

execute('scrapy crawl quotes'.split())
# print('scrapy crawl quotes'.split())