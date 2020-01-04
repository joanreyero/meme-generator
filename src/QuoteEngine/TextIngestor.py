from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        return cls.parse_text(path)


    @staticmethod
    def parse_text(path: str) -> List[QuoteMode]:
        file_ref = open(path, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                quotes.append(QuoteMode(parsed[0],
                                    parsed[1]))

        file_ref.close()
        return quotes
