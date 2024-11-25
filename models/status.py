from enum import Enum


class StatusEnum(str, Enum):
    SUCCESS = "success"
    PENDING = "pending"
    FAILURE = "failure"
