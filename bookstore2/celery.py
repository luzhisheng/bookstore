from __future__ import absolute_import,unicode_literals
import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','bookstore2.settings') #设置配置文件
django.setup()
app = Celery('bookstore2',broker='redis://127.0.0.1:6379/6')
app.config_from_object('django.conf:settings',namespace='CELERY') #制定celery配置文件
app.autodiscover_tasks() #任务

@app.task(bind=True)
def debug_task(self):
	print('Request:{0!r}'.format(self.request))