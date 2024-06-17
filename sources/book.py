from generics import Editors, Source, input_bool, Online, Pages, Title
from typing import override


ORDINAL_SUFFIXES = {
    0: "th",
    1: "st",
    2: "nd",
    3: "rd",
    4: "th",
    5: "th",
    6: "th",
    7: "th",
    8: "th",
    9: "th"
}


class Book(Source):
    """This source represents an entire book, be it online or print only. This also includes kindle and other e-reader books.
    
    To reference a specific chapter, use the Chapter source instead.
    """
    
    def __init__(self):
        super().__init__()
        self.title = Title("Book")
        self.volume = 0
        self.edition_no = 0
        self.editors = Editors()
        self.city = ""
        self.usa = False
        self.state = ""
        self.country = ""
        self.publisher = ""
        self.year = 0
        self.online = Online()
    
    @property
    def edition(self) -> str:
        """Formats the edition number correctly, assuming one has been provided.
        
        Uses the remainder (%) operator to determine the cardinal suffix (e.g. 1st, 2nd, 3rd) that's
        appropriate for the edition number.
        """
        
        return f"{self.edition_no}{ORDINAL_SUFFIXES[self.edition_no % 10]} ed"
    
    @override
    def ask(self):
        super().ask()
        self.title.ask()
        self.volume = int(input("Volume number (0 if not given): "))
        self.edition_no = int(input("Edition number (1 if not given): "))
        self.editors.ask()
        self.city = input("Publisher's city: ")

        self.usa = input_bool("Is the publisher from the USA?")
        if self.usa:
            self.country = "USA"
            self.state = input("Publisher's state (e.g. NJ, CA, etc): ")
            
            # TODO: check against a list of state codes
            
        self.publisher = input("Name of publisher: ")
        self.year = int(input("Year published: "))
        self.online.ask()
        
        # TODO: validate year, has to be in the past
        
    @override
    @property
    def ieee(self):
        out = super().ieee + f"*{self.title.ieee}*"
        
        if self.volume != 0:
            out += f", vol. {self.volume}"
        
        if self.edition_no > 1:
            out += f", {self.edition}"
            
        out += f". {self.editors.ieee}. {self.city}, "
        
        if self.usa:
            out += f"{self.state}, "
            
        out += f"{self.country}: {self.publisher}, {self.year}."
        
        if self.online.is_online:
            out += f" {self.online.ieee}"
        
        return out
    

class Chapter(Book):
    """A source for a single chapter in a book. If you want to reference multiple chapters,
    use multiple of these classes.
    
    Chapters can be online or print only, the class will do the work.
    """
    
    def __init__(self):
        super().__init__()
        self.chapter = ""
        self.pages = Pages()
        
    @override
    def ask(self):
        super().ask()
        self.chapter = input("Chapter title: ")
        self.pages.ask()
        
    @override
    @property
    def ieee(self):
        out = super(Book, self).ieee + f'"{self.chapter.capitalize()}," in *{self.title.ieee}*'
        
        if self.volume != 0:
            out += f", vol. {self.volume}"
        
        if self.edition_no > 1:
            out += f", {self.edition}"
            
        out += f". {self.editors.ieee}. {self.city}, "
        
        if self.usa:
            out += f"{self.state}, "
            
        out += f"{self.country}: {self.publisher}, {self.year}, {self.pages.ieee}."
        
        if self.online.is_online:
            out += f" {self.online.ieee}"
        
        return out
    