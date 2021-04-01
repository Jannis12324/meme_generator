"""Wrapper to pull together different ingestor classes."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CsvIngestor import CsvIngestor
from .DocxIngestor import DocxIngestor
from .TxtIngestor import TxtIngestor
from .PdfIngestor import PdfIngestor


class Ingestor(IngestorInterface):
    """
    Encapsulation for the file ingestors that manages which one is appropriate.

    Returns a list of Quote Models.
    """

    importers = [PdfIngestor, TxtIngestor, DocxIngestor, CsvIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Iterate through the defined ingestors and check with
         their can_ingest methods if they are suitable.

        Return: List of Quote Models
        """
        for ingestor in cls.importers:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
