from .input import input_bool
from typing import override


class Contributor:
    """Base class for all authors and editors, including people and companies.
    
    This mostly just exists to ensure both types follow the same format and thus the rest of the code
    doesn't care which one it's using.
    """
    
    def ask(self):
        """Requests details of the contributor's name from the user."""
        
        raise NotImplemented

    @property
    def ieee(self) -> str:
        """Returns the contributor's name in IEEE format."""
        
        raise NotImplemented


class Person(Contributor):
    """A type of contributor that refers to a specific person.
    
    In IEEE, people are referenced as follows: I. Surname
    If the person has multiple forenames (e.g. a first name and middle names), initials should be given for each forename.
    """
    
    def __init__(self):
        self.names: list[str] = []
        self.surname = ""
        
    @property
    def initials(self):
        """Returns the initials of the person.
        
        This includes the initials of any middle names that the person has.
        """
        
        return " ".join([f"{n[0].capitalize()}." for n in self.names])
    
    @override
    def ask(self):
        """Inputs the person's forenames and surname."""
        
        self.names = input("Forename(s) separate by spaces: ").split(" ")
        self.surname = input("Surname: ")
    
    @override
    @property
    def ieee(self):
        """Returns the person's name in IEEE format."""
        
        return f"{self.initials} {self.surname.title()}"


class Company(Contributor):
    def __init__(self):
        self.name = ""
        
    @override
    def ask(self):
        """Asks for the company's name. This is just a simple string."""
        
        self.name = input("Company name: ")
        
    @override
    @property
    def ieee(self):
        """Returns the company's name in IEEE format...which is literally just the company's name."""
        
        return self.name.title()
    
    
class Contributors:
    """Base class for the author and editor handlers.
    
    I didn't want to duplicate any code, so I made this class. It doesn't actually have any usable data,
    it just has the base IEEE format for contributors. Since editors is literally just authors but with Ed(s)
    added to the end, we can use the same function for both.
    """
    
    def __init__(self):
        self.contributors: list[Person | Company] = []

    def ask(self):
        """Gets the list of contributors for the source."""
        
        raise NotImplemented

    @property
    def ieee(self) -> str:
        """Generates a list of source contributors according to the IEEE standard.
        
        IEEE dictates three different formats according to how many contributors there are:
            - One contributor: I. Surname
            - Multiple contributors: I. Surname, I. Surname and I. Surname
            - More than 6 contributors: I. Surname, et al.S
        Note: corporate contributors don't have initials and surnames, so just use the name of the company.
        """
        
        match n := len(self.contributors):
            # Return first author followed by et al
            case _ if n > 6:
                return f"{self.contributors[0].ieee}, *et al.*"
            
            # Join with a comma except with the last where we join with 'and' instead 
            case _ if 1 < n <= 6:
                return ", ".join([n.ieee for n in self.contributors[:len(self.contributors) - 1]]) + f" and {self.contributors[-1].ieee}"
                
            case _ if n == 1:
                return self.contributors[0].ieee


class Authors(Contributors):
    """This is the main handler for requesting and formatting authors of a source in the IEEE standard.
    
    Thankfully, IEEE is very nice and the format for authors doesn't change across source types, so we can use a
    single handler.
    """
        
    @override
    def ask(self):
        while True:
            corp = input_bool("Corporate author?")
            
            author = Company() if corp else Person()
            author.ask()
            self.contributors.append(author)
            
            # Ask if there's any more authors to add
            if not input_bool("Add another author?"):
                break

                
class Editors(Contributors):
    """This is the main handler for requesting and formatting editors of a source in the IEEE standard.
    
    This works very similarly to authors, but does not allow for corporate editors and has a slightly different format.
    """
        
    @override
    def ask(self):
        while True:
            editor = Person()
            editor.ask()
            self.contributors.append(editor)
            
            # Ask if there's any more editors to add
            if not input_bool("Add another editor?"):
                break
    
    @override
    @property
    def ieee(self) -> str:
        """Generates a list of source editors according to the IEEE standard."""
        
        if len(self.contributors) > 1:
            return f"{super().ieee}, Eds"
        
        return f"{super().ieee}, Ed"
