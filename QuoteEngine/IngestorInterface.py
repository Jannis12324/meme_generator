"""Abstract base class that defines the interface for the ingestors."""

from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Abstract base class that implements the interface for the extending file ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the extension of the filepath is in the list of allowed extensions."""
        return path.split(".")[-1] in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Interface definition for overrides in extending classes."""
        pass
