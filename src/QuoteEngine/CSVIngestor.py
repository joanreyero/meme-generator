from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode


class CSVIngestor(IngestorInterface):
    """Parses a .csv file and returns a list of quotes."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parses a .csv file and returns a list of quotes.
        Arguments:
        path {str}: the path to the file to parse.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        # Read the CSV and turn to Pandas DataFrame.
        df = pd.read_csv(path, header=0)

        # Create the quotes from the rows
        for index, row in df.iterrows():
            quotes.append(QuoteMode(row['body'], row['author']))

        return quotes
