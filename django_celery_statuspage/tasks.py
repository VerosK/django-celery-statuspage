from __future__ import absolute_import
from celery import shared_task
import datetime



@shared_task(name='celery_status_page.ping_task', bind=True, rate_limit='60/m', timeout=60)
def ping_task(sef):
    retv = dict(
        response = 'pong'
    )
    return retv

