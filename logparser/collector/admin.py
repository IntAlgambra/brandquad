from django.contrib import admin

from .models import LogRecord


@admin.register(LogRecord)
class LogRecordAdmin(admin.ModelAdmin):
    list_display = ("ip", "log_time", "method", "endpoint", "response_code")
    list_filter = ("log_time", "response_code")
    search_fields = ("ip",)
