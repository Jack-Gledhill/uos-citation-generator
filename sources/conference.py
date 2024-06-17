from generics import Source, Title, Pages, Online, input_bool
from typing import override


class UnpublishedConferencePaper(Source):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.name = Title("Conference")
        self.location = ""
        self.year = 0
        self.online = Online()
        
    @override
    def ask(self):
        super().ask()
        self.title = input("Paper title: ")
        self.name.ask()
        
        if input_bool("Do you know the location of the conference?"):
            self.location = input("Conference location: ")
            
        if not input_bool("Is the conference year already in the name of the conference?"):
            self.year = int(input("Conference year: "))
            
        self.online.ask()
        
    @override
    @property
    def ieee(self) -> str:
        out = super().ieee + f'"{self.title}," presented at the {self.name.ieee}, '
        if self.location != "":
            out += f"{self.location}, "
            
        if self.year != 0:
            out += f"{self.year}."
        
        if self.online.is_online:
            out += f" {self.online.ieee}"
            
        return out


class PublishedConferencePaper(UnpublishedConferencePaper):
    def __init__(self):
        super().__init__()
        self.pages = Pages()
        
    @override
    def ask(self):
        super().ask()
        self.pages.ask()
        
    @override
    @property
    def ieee(self) -> str:
        out = super(UnpublishedConferencePaper, self).ieee + f'"{self.title}," in *{self.name.ieee}*, '
        if self.location != "":
            out += f"{self.location}, "
            
        if self.year != 0:
            out += f"{self.year}, "
            
        out += f"{self.pages.ieee}."
        
        if self.online.is_online:
            out += f" {self.online.ieee}"
            
        return out
            