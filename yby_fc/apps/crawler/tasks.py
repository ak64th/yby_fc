from celery import shared_task
from scrapy.crawler import CrawlerProcess

from yby_fc.apps.crawler.spiders.bilibili import BilibiliSpider


@shared_task()
def crawl():
    process = CrawlerProcess()
    process.crawl(BilibiliSpider)
    process.start()
