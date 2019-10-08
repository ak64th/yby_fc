import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from yby_fc.apps.crawler.crawl import crawl_bilibili_search_page


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--within-days',
            dest='days',
            type=int,
            default=30
        )

    def handle(self, *args, **options):
        within_days = options['days']
        back_to = (timezone.now() - datetime.timedelta(within_days)
                   if within_days else None)
        crawl_bilibili_search_page(back_to)
