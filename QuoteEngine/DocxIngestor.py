"""Ingests docx files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import docx


class DocxIngestor(IngestorInterface):
    """A class that handles the ingestion of docx files."""

    allowed_extensions = ["docx"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse QuoteModel objects of docx files and return a list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        doc = docx.Document(path)

        for line in doc.paragraphs:
            if line.text != "":
                parse = line.text.split('-')
                new_cat = QuoteModel(str(parse[0]).strip(' "'), str(parse[1]).strip(' "'))
                quotes.append(new_cat)

        return quotes
