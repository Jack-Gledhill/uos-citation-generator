from .input import input_bool


class Online:
    """Handler for source URLs and dois.
    
    The format for this is the same across basically every source type, so it needs to be made a generic.
    """
    
    def __init__(self):
        self.link = ""
        
    @property
    def is_online(self) -> bool:
        """Determines whether the source is online or not by checking if a URL or doi was given."""
        
        return self.link != ""
    
    @property
    def link_type(self) -> str:
        """Checks whether the set link is a URL or a doi.
        
        This assumes that URLs will always start with http (which is how they should be in IEEE).
        """
        
        if self.link.lower().startswith("http"):
            return "URL"
        
        return "doi"
        
    def ask(self):
        """Asks if the source is available online, then asks for the URL or doi."""
        
        if input_bool("Is this source available online?"):
            self.link = input("URL or doi: ").lower()
            
    @property
    def ieee(self) -> str:
        """Outputs the source's URL or doi in the standard IEEE format.
        
        There's only one exception where this format is NOT used, which is unpublished journal articles.
        """
        
        if self.link_type == "URL":
            return f"[Online]. Available: {self.link}"
        
        return f"[Online]. doi: {self.link}."
        