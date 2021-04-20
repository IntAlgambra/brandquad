from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import LogRecord

from django.db import models

from .datamodels import Record


class LogRecordManager(models.Manager):

    def create_record(self, record_model: Record) -> LogRecord:
        record = self.model(
            ip=str(record_model.ip),
            log_time=record_model.log_time,
            method=record_model.method,
            endpoint=record_model.endpoint,
            protocol=record_model.protocol,
            response_code=record_model.response_code,
            respose_size=record_model.response_size,
            referer=record_model.referer,
            user_agent=record_model.user_agent
        )
        record.save()
        return record
