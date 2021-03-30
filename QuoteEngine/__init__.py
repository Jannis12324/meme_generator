"""Import all Ingestors and make them available upon package import."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CsvIngestor import CsvIngestor
from .DocxIngestor import DocxIngestor
from .TxtIngestor import TxtIngestor
from .PdfIngestor import PdfIngestor
from .Ingestor import Ingestor

