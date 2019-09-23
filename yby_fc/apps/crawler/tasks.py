from celery import shared_task
from django.conf import settings
from scrapy.crawler import CrawlerProcess

from yby_fc.apps.crawler.spiders.bilibili import BilibiliSpider


@shared_task()
def crawl():
    crawler_settings = getattr(settings, 'CRAWLER_SETTINGS', None)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(BilibiliSpider)
    process.start()
