from __future__ import absolute_import
from celery.exceptions import TimeoutError
from django.http import HttpResponse
from django_celery_statuspage.tasks import ping_task
import traceback

TIMEOUT = 5

def ping(request):
    try:
        async_result = ping_task.delay()
    except:
        content = "Error\nProblem in Celery config. Unable to queue task\n--\n"
        content += traceback.format_exc() 
        return HttpResponse(
            content=content,
            content_type='text/plain',
            status=500)
    try:
        lazy_result = async_result.get(timeout=TIMEOUT)
    except TimeoutError:
        return HttpResponse(
            content="Error\nCelery task was not executed in {} seconds".format(TIMEOUT),
            content_type='text/plain',
            status=500)
    return HttpResponse(
        content="OK\nCelery is running. Task was executed and result was reported.",
        content_type='text/plain',
    )
