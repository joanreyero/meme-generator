

class QuoteMode():
    """ The Quote object.
    Attributes:
    - body {str}: the body of the quote.
    - author {str}: the author of the quote.
    """
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Use a '"body" - author' format to represent
        the quote.
        """
        return f'"{self.body}" - {self.author}'
