from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from django.conf import settings

from yby_fc.apps.crawler.spiders.bilibili import BilibiliSpider


class Command(BaseCommand):
    def handle(self, *args, **options):
        crawler_settings = getattr(settings, 'CRAWLER_SETTINGS', None)
        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(BilibiliSpider)
        process.start()
