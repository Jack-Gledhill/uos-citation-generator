from generics import Source, PublishDate
from typing import override


class Email(Source):
    """This is called email but could really refer to any kind of private communication.
    
    Remember: you need the sender's permission to use this as a referenced work.
    """
    
    def __init__(self):
        super().__init__()
        self.sent = PublishDate()
        
    @override
    def ask(self):
        super().ask()
        self.sent.ask()
        
    @override
    @property
    def ieee(self) -> str:
        return super().ieee + f"private communication, {self.sent.ieee}"
    