import datetime

from celery import shared_task
from django.utils import timezone

from yby_fc.apps.crawler.crawl import crawl_bilibili_search_page as _do_crawl


@shared_task()
def crawl_bilibili_search_page(within_days=None):
    back_to = (timezone.now() - datetime.timedelta(within_days)
               if within_days else None)
    _do_crawl(back_to)
