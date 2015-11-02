
# django-celery-statuspage

This is simple module which can be used to test running Celery tasks.

Usage:

 * add `django_celery_statuspage` to your APPLICATIONS

 * add `url('^/status/celery/', 'django_celery_status.views.ping_view')`,
   to your url definition

 * open `/status/celery/` page on your website

Opening `/status/celery/` page creates one dummy task, runs it and 
returns its result. If the task result is not obtained withing 5 seconds,
response is 500.

The `/status/celery/` page can be added to your Nagios/Icinga monitoring.
