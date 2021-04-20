from django.utils import timezone
from django.test import SimpleTestCase
from pydantic import ValidationError

from collector.datamodels import Record


class TestLogRecordDatamodel(SimpleTestCase):
    TEST_DATA = {
        "ip": "13.66.139.0",
        "log_time": timezone.now(),
        "method": "GET",
        "endpoint": "/index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53",
        "protocol": "HTTP/1.1",
        "response_code": 200,
        "response_size": 32123,
        "referer": "http://www.almhuette-raith.at/",
        "user_agent": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)"
    }

    def testValidData(self):
        Record(**self.TEST_DATA)

    def testInvalidIp(self):
        data = {
            **self.TEST_DATA,
            "ip": "43.123.3232.123.443"
        }
        with self.assertRaises(ValidationError):
            Record(**data)

    def testInvalidMethod(self):
        data = {
            **self.TEST_DATA,
            "method": "RETRIEVE"
        }
        with self.assertRaises(ValidationError):
            Record(**data)

    def testInvalidResponseCode(self):
        data = {
            **self.TEST_DATA,
            "response_code": 100500
        }
        with self.assertRaises(ValidationError):
            Record(**data)

    def testInvalidReferer(self):
        data = {
            **self.TEST_DATA,
            "referer": "someweb.kek"
        }
        with self.assertRaises(ValidationError):
            Record(**data)

    def testInvalidResponseSize(self):
        data = {
            **self.TEST_DATA,
            "response_size": 123.74
        }
        with self.assertRaises(ValidationError):
            Record(**data)

    def testInvalidEndpoint(self):
        data = {
            **self.TEST_DATA,
            "endpoint": "no/slash/index.php"
        }
        with self.assertRaises(ValidationError):
            Record(**data)
