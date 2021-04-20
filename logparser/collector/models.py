from django.db import models

from .managers import LogRecordManager


class LogRecord(models.Model):
    ip = models.GenericIPAddressField()
    log_time = models.DateTimeField()
    method = models.CharField(max_length=7)
    endpoint = models.TextField()
    protocol = models.CharField(max_length=25)
    response_code = models.IntegerField()
    respose_size = models.IntegerField()
    referer = models.URLField(null=True, max_length=1000)
    user_agent = models.TextField()

    objects = LogRecordManager()
