class Pages:
    """Handles formatting page numbers within sources.
    
    This is commonly used when referencing books or articles in journals. There's a different format for sources
    spanning one page and sources spanning multiple pages, so making a separate handler is a wise idea.
    """
    
    def __init__(self):
        self.start = 0
        self.end = 0
        
    def ask(self):
        """Asks for the first and last page numbers of the source."""
        
        self.start = int(input("First page: "))
        self.end = int(input("Last page: "))
        
        # TODO: validation, can't end before it starts etc
        
    @property
    def ieee(self) -> str:
        """Generates the page numbers in the IEEE format."""
        
        # Source only spans one page, use p. x
        if self.start == self.end:
            return f"p. {self.start}"
        
        # Source spans multiple pages, use pp. x-y
        return f"pp. {self.start}-{self.end}"
        