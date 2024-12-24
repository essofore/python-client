from enum import Enum


class MetadataMode(str, Enum):
    REPLACE = "REPLACE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
