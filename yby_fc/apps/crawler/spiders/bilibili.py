import bs4
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']

    def start_requests(self):
        yield scrapy.Request(
            url='https://search.bilibili.com/all?keyword=杨冰怡&order=pubdate',
        )

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text)
        print(soup.prettify())
