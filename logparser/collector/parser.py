from typing import Optional
from datetime import datetime
import re

from collector.datamodels import Record

REFERER_PATTERN = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'


def validate_url(url: str) -> Optional[str]:
    if re.fullmatch(REFERER_PATTERN, url):
        return url
    return


def parse_apache_datetime(apache_time: str) -> datetime:
    """
    Преобразует datetime из apache формата в datetime объект
    """
    return datetime.strptime(apache_time, "%d/%b/%Y:%H:%M:%S %z")



def parse_record(record: str) -> Record:
    """
    Парсит одну строку из лога апача и возвращает модель данных
    """
    parts = record.split(" ")
    ip = parts[0]
    log_time = parse_apache_datetime(
        " ".join(
            (parts[3].strip("[]"),
             parts[4].strip("[]"))
        )
    )
    method = parts[5].strip('"')
    endpoint = parts[6]
    protocol = parts[7].strip('"')
    response_code = parts[8]
    response_size = parts[9]
    referer = (parts[10].strip('"')
               if validate_url(parts[10].strip('"'))
               else None)
    user_agent = " ".join(parts[11:-2]).strip('"')
    return Record(
        ip=ip,
        log_time=log_time,
        method=method,
        endpoint=endpoint,
        protocol=protocol,
        response_code=int(response_code),
        response_size=response_size,
        referer=referer,
        user_agent=user_agent
    )
