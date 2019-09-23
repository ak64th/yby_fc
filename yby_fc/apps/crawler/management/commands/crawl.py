from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess

from yby_fc.apps.crawler.spiders.bilibili import BilibiliSpider


class Command(BaseCommand):
    def handle(self, *args, **options):
        process = CrawlerProcess()
        process.crawl(BilibiliSpider)
        process.start()
