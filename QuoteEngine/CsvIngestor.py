"""Ingests csv files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import pandas as pd


class CsvIngestor(IngestorInterface):
    """A class that handles the ingestion of csv files."""

    allowed_extensions = ["csv"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse QuoteModel obj of csv files and return a list of them."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)
        return quotes
