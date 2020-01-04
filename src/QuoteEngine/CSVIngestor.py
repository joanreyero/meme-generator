from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quotes.append(QuoteMode(row['body'], row['author']))

        return quotes
