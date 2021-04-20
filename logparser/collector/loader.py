import requests
import uuid

from django.conf import settings

from pydantic import ValidationError

from .parser import parse_record
from .models import LogRecord


def load_log(url: str) -> None:
    """
    загружает и парсит лог-файл по строкам.
    Если строка не является валидной записью, то просто пропускаем
    ее (по хорошему ошибки бы логгировать, но в тестовом можно этого не делать)
    А еще фукцию можно было бы обернуть в transaction.atomic() чтобы при ошибках
    в БД ничего не записывалось.
    """
    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        if not line:
            continue
        try:
            record = parse_record(line.decode())
        except IndexError:
            # обработка случая, в котором у все строки невалидная структура
            continue
        except ValidationError:
            # обработка случая, когда какие-либо данные в логе невалидны
            continue
        LogRecord.objects.create_record(record)
