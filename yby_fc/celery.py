import os
from celery import Celery

# if python-dotenv is installed, read .env
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        pass

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yby_fc.settings')

app = Celery('yby_fc')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
