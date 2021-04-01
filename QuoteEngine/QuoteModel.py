"""Class to represent a quote."""


class QuoteModel:
    """A class representing a quote with body and author."""

    def __init__(self, body: str, author: str):
        """Set up a Quote Model with author and body."""
        self.body = str(body)
        self.author = str(author)

    def __str__(self):
        """Override the string representation of a QuoteModel object."""
        return f"Quote Model of Author {self.author} and the quote {self.body}"

    def __repr__(self):
        """Override the machine representation of a QuoteModel object."""
        return f"QuoteModel object. Author: {self.author}, body: {self.body}"
