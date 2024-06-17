from generics import AccessDate, Source, Title, FullDate
from typing import override
        

class Webpage(Source):
    """This is an undated web page on a website.
    
    If the webpage has a date, you should be using a WebArticle instead.
    """
    
    def __init__(self):
        super().__init__()
        self.title = ""
        self.website = Title("Website")
        self.url = ""
        self.accessed = AccessDate()
    
    @override
    def ask(self):
        super().ask()
        self.title = input("Title of page: ")
        self.website.ask()
        self.url = input("URL: ")
        self.accessed.ask()
        
    @override
    @property
    def ieee(self):
        # TODO: make sure IBM says in all caps
        
        return super().ieee + f'"{self.title.capitalize()}." {self.website.ieee}. {self.url} {self.accessed.ieee}.'
        

class Blog(Webpage):
    """A source type specifically for online blog posts.
    
    These are separate to webpages and web articles, so be careful not to confuse them.
    """
    
    def __init__(self):
        super().__init__()
        self.published = FullDate()
        self.accessed = FullDate()
        
    @override
    def ask(self):
        super().ask()
        self.published.ask()
        
    @override
    @property
    def ieee(self) -> str:
        return super(Webpage, self).ieee + f'"{self.title.capitalize()}," in *{self.website.ieee}*, {self.published.ieee}. [Blog]. Accessed: {self.accessed.ieee}. Available: {self.url}'
        