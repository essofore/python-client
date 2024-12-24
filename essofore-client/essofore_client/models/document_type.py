from enum import Enum


class DocumentType(str, Enum):
    DOC = "DOC"
    HTML = "HTML"
    PDF = "PDF"
    PPT = "PPT"
    TXT = "TXT"
    XLS = "XLS"

    def __str__(self) -> str:
        return str(self.value)
