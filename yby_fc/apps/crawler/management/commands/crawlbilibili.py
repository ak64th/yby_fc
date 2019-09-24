import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from yby_fc.apps.crawler.tasks import crawl


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--within-days',
            dest='days',
            type=int,
            default=30
        )

    def handle(self, *args, **options):
        back_to = timezone.now() - datetime.timedelta(options['days'])
        crawl.apply(kwargs={'back_to': back_to}, throw=True)
