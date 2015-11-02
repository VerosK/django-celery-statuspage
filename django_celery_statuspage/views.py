from __future__ import absolute_import
from celery.exceptions import TimeoutError
from django.http import HttpResponse
from django_celery_statuspage.tasks import ping_task

TIMEOUT = 5

def ping(request):
    async_result = ping_task.delay()
    try:
        lazy_result = async_result.get(timeout=TIMEOUT)
    except TimeoutError:
        return HttpResponse(
            content="Error\nCelery task was not executed in {} seconds".format(TIMEOUT),
            content_type='text/plain',
            status=500)
    return HttpResponse(
        content="OK\nCelery is running. Celery was executed and got result",
        content_type='text/plain',
    )