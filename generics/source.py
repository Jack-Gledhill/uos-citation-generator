from .contributors import Authors


class Source:
    """Generic base class that all sources inherit from.
    
    This already includes the author handler, so sources just need to handle their own variables.
    """
    
    def __init__(self):
        self.authors = Authors()

    def ask(self):
        """Asks for the source's variables from the user."""
        
        self.authors.ask()

    @property
    def ieee(self) -> str:
        """Generates the full reference for this source.
        
        The base function generates the reference number and authors list for you, so just call super().ieee
        instead of writing them out every time.
        """
        
        return f"[1] {self.authors.ieee}, "
