"""Ingests txt files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """A class that handles the ingestion of txt files."""

    allowed_extensions = ["txt"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse QuoteModel objects of txt files and return a list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        with open(path, "r", encoding="utf-8-sig") as infile:
            lines = infile.readlines()

        quotes = []
        for line in lines:
            line = line.replace("\n", "")
            line = line.split("-")
            quote = QuoteModel(line[0].strip(), line[1].strip())
            quotes.append(quote)
        return quotes
