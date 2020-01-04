from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode


class TextIngestor(IngestorInterface):
    """Parses a .txt file and returns a list of quotes."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """ Checks whether the file can be ingested and
        calls the txt parser.
        Arguments:
        path {str}: the path to the file to parse.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        return cls.parse_text(path)

    @staticmethod
    def parse_text(path: str) -> List[QuoteMode]:
        """Parses a .txt file and returns a list of quotes.
        Arguments:
        path {str}: the path to the file to parse.
        """
        file_ref = open(path, "r")
        quotes = []
        for line in file_ref.readlines():
            # Remove unwanted elements and spaces
            line = line.strip('\n\r').strip()
            if len(line) > 0:  # If there is a line
                parsed = line.split(' - ')  # Split
                # Create the Quote object
                quotes.append(QuoteMode(parsed[0],
                                        parsed[1]))

        file_ref.close()
        return quotes
