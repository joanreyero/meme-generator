from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode
from .TextIngestor import TextIngestor

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
        quotes = TextIngestor.parse_text(tmp)
        os.remove(tmp)
        return quotes