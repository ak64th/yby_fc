=================
YBY FAN CLUB SITE
=================

Built with Django 2.2, Django-rest-framework 3 and Python 3.6.


Development
-----------

Install requirements for development, assuming virtualenv is used.

.. code:: bash

   $ pip install -r requirements.txt
   $ pip install -r requirements_dev.txt

Create a .env file with following content:

.. code:: bash

   DJANGO_SETTINGS_MODULE=local_settings

Create local_settings.py:

.. code:: python

   # flake8: noqa
   from yby_fc.settings import *

   DEBUG = True
   ALLOWED_HOSTS = ['*']
   # more local settings

Run data migrations:

.. code:: bash

   python manage.py migrate

Run development server:

.. code:: bash

   python manage.py runserver
