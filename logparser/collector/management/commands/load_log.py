from django.core.management.base import BaseCommand, CommandError

from collector.parser import validate_url
from collector.loader import load_log


class Command(BaseCommand):
    help = 'loads apache access log file from url'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help="url to log file")

    def handle(self, *args, **options):
        url = options.get("url")
        if not validate_url(url):
            print("Invalid url provided!")
        load_log(url)


