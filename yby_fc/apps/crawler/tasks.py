from celery import shared_task
from django.conf import settings
from scrapy.crawler import CrawlerProcess

from yby_fc.apps.crawler.spiders.bilibili import BilibiliSpider


@shared_task()
def crawl(back_to=None):
    crawler_settings = getattr(settings, 'CRAWLER_SETTINGS', None)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(BilibiliSpider, back_to=back_to)
    process.start()
