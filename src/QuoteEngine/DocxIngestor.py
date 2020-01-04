from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode


class DocxIngestor(IngestorInterface):
    """Parses a .docx file and returns a list of quotes."""
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parses a .docx file and returns a list of quotes.
        Arguments:
        path {str}: the path to the file to parse.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        # Parse the document using python-docx
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                # Split and create the quote
                parse = para.text.split(' - ')
                quotes.append(QuoteMode(parse[0], parse[1]))

        return quotes
