from generics import Source
from typing import override


class Unpublished(Source):
    """This is for, you guessed it, unpublished documents/papers!
    
    Be careful using this one, you can't exactly fact-check it.
    """
    
    def __init__(self):
        super().__init__()
        self.title = ""
        
    @override
    def ask(self):
        super().ask()
        self.title = input("Title of document: ")
        
    @override
    @property
    def ieee(self) -> str:
        return super().ieee + f'"{self.title.capitalize()}," unpublished.'
