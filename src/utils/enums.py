from enum import Enum

# class syntax
class Table(Enum):
    USER = "USER"


class ResponseType(Enum):
    SUCCESS = "SUCCESS"
    CUSTOM_ERROR = "CUSTOM_ERROR"
    ERROR = "ERROR"