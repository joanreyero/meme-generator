from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteMode import QuoteMode
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Ingestor class that calls the appripiate importer."""
    importers = [DocxIngestor, CSVIngestor,
                 PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
