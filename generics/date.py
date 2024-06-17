from datetime import datetime
from .input import input_bool

MONTH_ABBREVS: dict[int, str] = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "July",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}


class AccessDate:
    """A generic handler for source access dates.
    
    Currently, this is only used for undated web pages. However, it has enough logic to warrant a generic handler
    in case it's ever used in the future.
    """
    
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0
        
    def ask(self):
        """Asks for the date that the source was accessed.
        
        If it was accessed today, it automatically grabs the date. Otherwise, it asks for it in the format: dd/mm/yyyy.
        """
        
        # Autofill if accessed today
        acc_today = input_bool("Did you access this source today?")
        if acc_today:
            self.day = datetime.now().day
            self.month = datetime.now().month
            self.year = datetime.now().year
            
        # Ask for full date if accessed earlier
        else:
            date = input("Date accessed (dd/mm/yyyy): ").split("/")
            self.day = int(date[0])
            self.month = int(date[1])
            self.year = int(date[2])
            
            # TODO: maybe add some validation here, check the date isn't in the future, etc
            
    @property
    def ieee(self) -> str:
        """Outputs the access date in IEEE format."""
        
        return f"(Accessed: {MONTH_ABBREVS[self.month]}. {self.day}, {self.year})"
    
    
class PublishDate:
    """Handler for source publish dates."""
    
    def __init__(self):
        self.month_known = False
        self.month = 0
        self.year = 0
        
    def ask(self):
        """Asks for the date that the source was published."""
        
        # TODO: validation, can't be in future, etc
        
        self.year = int(input("Year published: "))
        if input_bool("Do you know the month it was published?"):
            self.month_known = True
            self.month = int(input("Month published (1-12): "))
            
    @property
    def ieee(self) -> str:
        """Outputs the publish date in IEEE format."""
        
        if self.month_known:
            return f"{MONTH_ABBREVS[self.month]}. {self.year}"
        
        return f"{self.year}"
    

class FullDate:
    """Handler for full dates."""
    
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0
        
    def ask(self):
        """Asks for the date."""
        
        # TODO: validation, can't be in future, etc
        
        self.year = int(input("Year published: "))
        self.month = int(input("Month published (1-12): "))
        self.day = int(input("Day published (0-31): "))
            
    @property
    def ieee(self) -> str:
        """Outputs the full date in IEEE format."""
        
        return f"{MONTH_ABBREVS[self.month]}. {self.day}, {self.year}"
    