from generics import Title, Online


class Standard:
    """This source type is for referencing industry standards.
    
    This is one of the very few source types that does not inherit from Source, because it has no authors!
    """
    
    def __init__(self):
        self.title = Title("Standard")
        self.number = ""
        self.year = 0
        self.online = Online()
        
    def ask(self):
        self.title.ask()
        self.number = input("Standard number: ")
        self.year = int(input("Year: "))
        self.online.ask()
        
        # TODO: validate year
        
    @property
    def ieee(self) -> str:
        out = f"[1] *{self.title.ieee}*, {self.number}, {self.year}."
        
        if self.online.is_online:
            out += f" {self.online.ieee}"
            
        return out
    