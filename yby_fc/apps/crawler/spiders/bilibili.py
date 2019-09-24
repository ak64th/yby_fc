import datetime

import bs4
import dateutil.parser
import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    custom_settings = {
        'ITEM_PIPELINES': {
            'yby_fc.apps.crawler.pipelines.BilibiliPipeline': 300
        },
    }

    def __init__(self, back_to=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if back_to is not None:
            if isinstance(back_to, str):
                back_to = dateutil.parser.parse(back_to)
            elif not isinstance(back_to, datetime.date):
                raise ValueError(
                    'The `back_to` parameter should be a `datetime.date`',
                    ' object or string',
                )
        self.back_to = back_to

    def start_requests(self):
        yield scrapy.Request(
            url='https://search.bilibili.com/all?keyword=杨冰怡&order=pubdate',
        )

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text, features='lxml')
        print(self.back_to)
        print(soup.title.get_text())
