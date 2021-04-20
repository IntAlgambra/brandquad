from ipaddress import IPv4Address
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, AnyHttpUrl, validator


class Record(BaseModel):
    """
    Класс структурирует данные из записи лога и гарантирует,
    что в БД попадут только валидные данные
    """
    ip: IPv4Address
    log_time: datetime
    method: str
    endpoint: str
    protocol: str
    response_code: Any
    response_size: Any
    referer: Optional[AnyHttpUrl]
    user_agent: str

    @validator("method")
    def validate_method(cls, v: str) -> str:
        if v not in {"GET",
                     "POST",
                     "PUT",
                     "DELETE",
                     "PATH",
                     "OPTIONS",
                     "HEAD",
                     "CONNECT",
                     "TRACE"}:
            raise ValueError("not an http method")
        return v

    @validator("endpoint")
    def validate_endpoint(cls, v: str) -> str:
        if not v.startswith("/"):
            raise ValueError("endpoint must start with leading slash")
        return v

    @validator("response_code")
    def validate_code(cls, v: str) -> int:
        if int(v) < 100 or int(v) > 500:
            raise ValueError("response code must be between 100 and 500")
        return int(v)

    @validator("response_size")
    def validate_response_size(cls, v: str):
        if not v or v == "-":
            return 0
        if not v.isdigit():
            raise ValueError("response size not valid")
        return int(v)
        # if type(v) != int:
        #     raise TypeError("response size must be integer")
        # if v < 0:
        #     raise ValueError("response size cannot be negative")
        # return v
