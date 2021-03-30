"""Ingests pdf files and returns a list of QuoteModule Objects."""

from .IngestorInterface import IngestorInterface
from typing import List
from .QuoteModel import QuoteModel
import os
import subprocess


class PdfIngestor(IngestorInterface):
    """A class that handles the ingestion of pdf files."""

    allowed_extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse QuoteModel objects of pdf files and return a list of QuoteModels."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        quotes = []
        # creates a temporary file to save and read the output of pdftotext
        temp = f".to_be_deletet.txt"
        # call the pdftotext tool
        # -layout makes sure the newlines are kept, so iteration will work
        call = subprocess.call(["xpdf-tools-mac-4.03/bin64/pdftotext", "-layout", path, temp])
        # iterate through the created txt file
        with open(temp, "r") as infile:
            for line in infile.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split("-")
                    quote = QuoteModel(parsed[0], parsed[1])
                    quotes.append(quote)
        # Remove the created txt file.
        os.remove(temp)
        return quotes
