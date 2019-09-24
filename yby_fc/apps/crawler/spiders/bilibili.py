import datetime

import bs4
import dateutil.parser
import furl
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
        done = False
        soup = bs4.BeautifulSoup(response.text, features='lxml')
        for node in soup.select('.video-item'):
            time = node.select_one('.time').get_text().strip()
            if dateutil.parser.parse(time).date() < self.back_to.date():
                done = True
                break
            link = node.select_one('a.title')
            title = link.attrs['title']
            href = link.attrs['href']
            video_id = furl.furl(href).path.segments[-1]
            watch_num = node.select_one('.watch-num').get_text().strip()
            print(video_id, title, watch_num, time)
        if not done:
            f = furl.furl(response.url)
            page = int(f.query.params.get('page', 1))
            f.query.params['page'] = str(page + 1)
            yield scrapy.Request(f.url)
