from generics import Source, Pages, Title, PublishDate, Online
from typing import override


class Article(Source):
    """Base class for articles. Currently used for articles in journals and web articles, but not unpublished articles.
    
    Having a base class allows us to separate the two types of articles without duplicating any code.
    This type cannot be used standalone, it doesn't have an ieee property so will just return the base text instead.
    """
    
    def __init__(self):
        super().__init__()
        self.title = ""
        self.source = Title("Journal / website")
        self.published = PublishDate()
        
    @override
    def ask(self):
        super().ask()
        self.title = input("Article title: ")
        self.source.ask()
        self.published.ask()
        
        
class WebArticle(Article):
    """This source class is for DATED web pages, these are considered to be articles.
    
    For undated webpages, use the webpage class instead.
    """
    
    def __init__(self):
        super().__init__()
        self.website = ""
        self.online = Online()
        
    @override
    def ask(self):
        super().ask()
        self.online.ask()
        
    @override
    @property
    def ieee(self) -> str:
        return super().ieee + f'"{self.title.capitalize()}," *{self.source.ieee}*, {self.published.ieee}. {self.online.ieee}'


class JournalArticle(Article):
    """This class is for articles published in a journal.
    
    If the article has NOT been published yet, use PreprintArticle instead.
    """
    
    def __init__(self):
        super().__init__()
        self.volume = 0
        self.number = 0
        self.pages = Pages()
        self.online = Online()
        
    @override
    def ask(self):
        super().ask()
        self.volume = int(input("Volume number: "))
        self.number = int(input("Issue number: "))
        self.pages.ask()
        self.online.ask()
        
        # TODO: validate volume & issue number: make sure non zero etc
        
    @override
    @property
    def ieee(self) -> str:
        # Start of the reference
        out = super().ieee + f'"{self.title.capitalize()}," *{self.source.ieee}*, vol. {self.volume}, no. {self.number}, {self.pages.ieee}, {self.published.ieee}.'
        
        # Add the doi if available online
        if self.online.is_online:
            out += f" {self.online.ieee}"
        
        return out
    

class PreprintArticle(Source):
    """A journal article that has not yet been published.
    
    This type of article lacks volume, issue and page numbers, as well as a publish date.
    """
    
    def __init__(self):
        super().__init__()
        self.title = ""
        self.journal = Title("Journal")
        self.link = ""
        
    @property
    def link_type(self):
        """Returns a string indicating the type of link used for this source - either a URL or a doi.
        
        This is determined by checking whether the link starts with http, which would indicate a URL.
        """
        
        if self.link.startswith("http"):
            return "URL"
        
        return "doi"
        
    @override
    def ask(self):
        super().ask()
        self.title = input("Article title: ")
        self.journal.ask()
        self.link = input("URL / doi: ")
        
    @override
    @property
    def ieee(self) -> str:
        out = super().ieee + f'"{self.title.capitalize()}," *{self.journal.ieee}*, to be published. {self.link_type}: {self.link}'
        if self.link_type == "doi":
            out += "."
            
        return out
