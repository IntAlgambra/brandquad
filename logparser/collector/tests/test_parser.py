from django.test import SimpleTestCase

from collector.parser import parse_record


class TestParser(SimpleTestCase):

    def testValidNoReferer(self):
        """
        Тестирует, что запись лога без referer парсится без ошибок
        """
        record_string = '13.66.139.0 - - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"'
        parse_record(record_string)

    def testValidWithReferer(self):
        """
        Тестирует, что запись лога с refrer парсится без ошибок
        """
        record_string = '42.236.10.125 - - [19/Dec/2020:15:23:13 +0100] "GET /templates/jp_hotel/images/logo.jpg HTTP/1.1" 200 369 "http://www.almhuette-raith.at/" "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAWEIEML-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 baidu.sogo.uc.UCBrowser/11.9.4.974 UWS/2.13.1.48 Mobile Safari/537.36 AliApp(DingTalk/4.5.11) com.alibaba.android.rimet/10487439 Channel/227200 language/zh-CN" "-"'
        parse_record(record_string)

    def testInvaidString(self):
        """
        при строке неверного формата возбуждается IndexError (остальные ошибки
        перехватываются при создании Record)
        """
        invalid_string = '[19/Dec/2020:15:23:13 +0100] "GET /templates/jp_hotel/images/logo.jpg HTTP/1.1" 200 369 "http://www.almhuette-raith.at/" "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-CN; EML-AL00 Build/HUAW'
        with self.assertRaises(IndexError):
            parse_record(invalid_string)

