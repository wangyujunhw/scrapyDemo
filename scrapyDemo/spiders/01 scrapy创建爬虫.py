import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # 定义爬虫名称

    def start_requests(self):
        # 设置爬取目标的地址
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            # 'https://desk.zol.com.cn/bizhi/9996_119871_2.html',
        ]

        # 获取所有地址，有几个地址发送几个请求
        for url in urls:
            # 发送网络请求
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.body)
        # 获取页数
        page = response.url.split('/')[-2]
        # 根据页数设置文件名称
        filename = 'quotes-%s.html' % page
        # 写入文件的模式打开文件，如果没有该文件就创建该文件
        with open(filename, 'wb') as f:
            f.write(response.body)
        # 输出保存文件的名称
        self.log('Saved file %s' % filename)
        # CSS提取数据
        print('CSS提取数据')
        print(response.css('title').extract()) # 返回标签代码
        print(response.css('title::text').extract_first()) # 返回标签中的数据
        print(response.css('title::text')[0].extract()) # 返回标签中的数据
        # XPath提取数据 可以再熟悉一下XPath的语法
        print('XPath提取数据')
        print(response.xpath('//title/text()').extract_first())
        print(response.xpath('//title/text()'))
        # 获取所有信息
        for quote in response.xpath(".//*[@class='quote']"):
            # 获取名人名言文字信息
            text = quote.xpath(".//*[@class='text']/text()").extract_first()
            # 获取作者
            author = quote.xpath(".//*[@class='author']/text()").extract_first()
            # 获取标签
            tags = quote.xpath(".//*[@class='tag']/text()").extract()
            # 以字典形式输出信息
            print(dict(text=text, author=author, tags=tags))
            # 创建Item对象
            item = ScrapydemoItem(text=text, author=author, tags=tags)
            yield item

        # 学习下面的翻页功能
        for quote in response.xpath(".//*[@class='quote']"):
            # 获取作者
            author = quote.xpath(".//*[@class='author']/text()").extract_first()
            print(author)
            # 实现翻页
            for href in response.css('li.next a::attr(href)'):
                yield response.follow(href, self.parse)

# 创建Items


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义获取名人名言文字信息
    text = scrapy.Field()
    # 定义获取的作者
    author = scrapy.Field()
    # 定义获取的标签
    tags = scrapy.Field()

    pass

