from typing import List
import subprocess
import os
import random
from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode
from .TextIngestor import TextIngestor


class PDFIngestor(IngestorInterface):
    """Parses a .pdf file and returns a list of quotes."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parses a .pdf file and returns a list of quotes.
        Arguments:
        path {str}: the path to the file to parse.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        # Create a temporary file
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        # Convert the PDF to text using pdftotex and subprocess
        call = subprocess.call(['pdftotext', '-layout', path, tmp])
        # Use the text parser in TextIngestor
        quotes = TextIngestor.parse_text(tmp)
        os.remove(tmp)
        return quotes
