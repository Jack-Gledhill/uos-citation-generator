# As given by http://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE_Reference_Guide.pdf
COMMON_ABBREVS: dict[str, str] = {
    "abstracts": "abstr",
    "academy": "acad",
    "accelerator": "accel",
    "acoustics": "acoust",
    "active": "act",
    "administration": "admin",
    "administrative": "administ",
    "advanced": "adv",
    "aeronautics": "aeronaut",
    "aerospace": "aerosp",
    "affective": "affect",
    "africa": "afr",
    "african": "afr",
    "aircraft": "aircr",
    "algebraic": "algebr",
    "american": "amer",
    "analysis": "anal",
    "annals": "ann",
    "annual": "annu",
    "apparatus": "app",
    "applications": "appl",
    "applied": "appl",
    "approximate": "approx",
    "architecture": "archit",
    "archive": "arch",
    "archives": "arch",
    "artificial": "artif",
    "assembly": "assem",
    "association": "assoc",
    "astronomy": "astron",
    "astronautics": "astronaut",
    "astrophysics": "astrophys",
    "atmosphere": "atmos",
    "atomic": "at",
    "atoms": "at",
    "australasian": "australas",
    "australia": "aust",
    "automatic": "autom",
    "automation": "automat",
    "automotive": "automot",
    "autonomous": "auton",
    "behaviour": "behav",
    "behavioural": "behav",
    "belgian": "belg",
    "biochemical": "biochem",
    "bioinformatics": "bioinf",
    "biology": "biol",
    "biological": "biol",
    "biomedical": "biomed",
    "biophysics": "biophys",
    "british": "brit",
    "broadcasting": "broadcast",
    "bulletin": "bull",
    "bureau": "bur",
    "business": "bus",
    "canadian": "can",
    "ceramic": "ceram",
    "chemical": "chem",
    "chinese": "chin",
    "climatology": "climatol",
    "clinical": "clin",
    "cognitive": "cogn",
    "colloquium": "colloq",
    "communications": "commun",
    "compatibility": "compat",
    "component": "compon",
    "components": "compon",
    "computational": "comput",
    "computer": "comput",
    "computers": "comput",
    "computing": "comput",
    "condensed": "condens",
    "conference": "conf",
    "congress": "congr",
    "consumer": "consum",
    "conversion": "convers",
    "convention": "conv",
    "correspondence": "corresp",
    "critical": "crit",
    "crystal": "cryst",
    "crystallography": "crystallogr",
    "cybernetics": "cybern",
    "decision": "decis",
    "delivery": "del",
    "department": "dept",
    "design": "des",
    "detector": "detect",
    "development": "develop",
    "developmental": "develop",
    "differential": "differ",
    "digest": "dig",
    "digital": "digit",
    "disclosure": "discl",
    "discussions": "discuss",
    "dissertations": "diss",
    "distributed": "distrib",
    "dynamics": "dyn",
    "earthquake": "earthq",
    "economic": "econ",
    "economics": "econ",
    "edition": "ed",
    "education": "educ",
    "electrical": "elect",
    "electrification": "electrific",
    "electromagnetic": "electromagn",
    "electroacoustic": "electroacoust",
    "electronic": "electron",
    "emerging": "emerg",
    "engineering": "eng",
    "environment": "environ",
    "equations": "equ",
    "equipment": "equip",
    "ergonomics": "ergonom",
    "european": "eur",
    "evaluation": "eval",
    "evolutionary": "evol",
    "exhibition": "exhib",
    "experimental": "exp",
    "exploratory": "explor",
    "exposition": "expo",
    "express": "exp",
    "fabrication": "fabr",
    "faculty": "fac",
    "ferroelectrics": "ferroelect",
    "francais": "fr",
    "french": "fr",
    "frequency": "freq",
    "foundation": "found",
    "fundamental": "fundam",
    "generation": "gener",
    "geology": "geol",
    "geophysics": "geophys",
    "geoscience": "geosci",
    "graphics": "graph",
    "guidance": "guid",
    "harmonic": "harmon",
    "harmonics": "harmon",
    "history": "hist",
    "horizon": "horiz",
    "hungary": "hung",
    "hungarian": "hung",
    "hydraulics": "hydraul",
    "hydrology": "hydrol",
    "illuminating": "illum",
    "imaging": "imag",
    "industrial": "ind",
    "information": "inf",
    "informatics": "inform",
    "innovation": "innov",
    "institute": "inst",
    "instrument": "instrum",
    "instrumentation": "instrum",
    "insulation": "insul",
    "integrated": "integr",
    "intelligence": "intell",
    "intelligent": "intell",
    "interactions": "interact",
    "international": "int",
    "isotopes": "isot",
    "israel": "isr",
    "japan": "jpn",
    "journal": "j",
    "knowledge": "knowl",
    "laboratory": "lab",
    "laboratories": "lab",
    "language": "lang",
    "learning": "learn",
    "letter": "lett",
    "letters": "lett",
    "lightwave": "lightw",
    "logic": "log",
    "logical": "log",
    "luminescence": "lumin",
    "machine": "mach",
    "magazine": "mag",
    "magnetics": "magn",
    "manufacturing": "manuf",
    "marine": "mar",
    "material": "mater",
    "mathematical": "math",
    "mathematics": "math",
    "measurement": "meas",
    "mechanical": "mech",
    "medical": "med",
    "medicine": "med",
    "metals": "met",
    "metallurgy": "metall",
    "meteorology": "meteorol",
    "metropolitan": "metrop",
    "mexican": "mex",
    "mexico": "mex",
    "microelectromechanical": "microelectromech",
    "microgravity": "microgr",
    "microscopy": "microsc",
    "microwave": "microw",
    "microwaves": "microw",
    "military": "mil",
    "modeling": "model",
    "molecular": "mol",
    "monitoring": "monit",
    "multiphysics": "multiphys",
    "nanobioscience": "nanobiosci",
    "nanotechnology": "nanotechnol",
    "national": "nat",
    "naval": "nav",
    "navigation": "navig",
    "network": "netw",
    "networking": "netw",
    "newsletter": "newslett",
    "nondestructive": "nondestruct",
    "nuclear": "nucl",
    "numerical": "numer",
    "observations": "observ",
    "oceanic": "ocean",
    "oceanography": "oceanogr",
    "occupation": "occupat",
    "operational": "oper",
    "optical": "opt",
    "optics": "opt",
    "optimization": "optim",
    "organisation": "org",
    "packaging": "packag",
    "particle": "part",
    "patent": "pat",
    "performance": "perform",
    "personal": "pers",
    "philosophical": "philos",
    "photonics": "photon",
    "photovoltaics": "photovolt",
    "physics": "phys",
    "physiology": "physiol",
    "planetary": "planet",
    "pneumatics": "pneum",
    "pollution": "pollut",
    "polymer": "polym",
    "polytechnic": "polytech",
    "practice": "pract",
    "precision": "precis",
    "principles": "princ",
    "proceedings": "proc",
    "processing": "process",
    "production": "prod",
    "productivity": "productiv",
    "programmable": "program",
    "programming": "program",
    "progress": "prog",
    "propagation": "propag",
    "psychology": "psychol",
    "quality": "qual",
    "quarterly": "quart",
    "radiation": "radiat",
    "radiology": "radiol",
    "reactor": "react",
    "receivers": "receiv",
    "recognition": "recognit",
    "record": "rec",
    "rehabilitation": "rehabil",
    "reliability": "rel",
    "report": "rep",
    "research": "res",
    "resonance": "reson",
    "resources": "resour",
    "review": "rev",
    "robotics": "robot",
    "royal": "roy",
    "safety": "saf",
    "satellite": "satell",
    "scandinavian": "scand",
    "science": "sci",
    "section": "sect",
    "security": "secur",
    "seismology": "seismol",
    "selected": "sel",
    "semiconductor": "semicond",
    "sensing": "sens",
    "series": "sre",
    "simulation": "simul",
    "singapore": "singap",
    "sistema": "sist",
    "society": "soc",
    "sociological": "sociol",
    "software": "softw",
    "solar": "sol",
    "soviet": "sov",
    "spectroscopy": "spectrosc",
    "spectrum": "specul",
    "statistics": "statist",
    "structure": "struct",
    "studies": "stud",
    "superconductivity": "supercond",
    "supplement": "suppl",
    "surface": "surf",
    "survey": "surv",
    "sustainable": "sustain",
    "symposium": "symp",
    "systems": "syst",
    "technical": "tech",
    "techniques": "techn",
    "technology": "technol",
    "telecommunications": "telecommun",
    "television": "telev",
    "temperature": "temp",
    "terrestrial": "terr",
    "theoretical": "theor",
    "transactions": "trans",
    "translation": "transl",
    "transmission": "transmiss",
    "transportation": "transp",
    "tutorials": "tut",
    "ultrasonic": "ulstrason",
    "university": "univ",
    "vacuum": "vac",
    "vehicular": "veh",
    "vibration": "vib",
    "vision": "vis",
    "visual": "vis",
    "welding": "weld",
    "working": "work"
}

# NOTE: make sure that all the words in this list are in LOWERCASE
INSIGNIFICANT_WORDS: list[str] = [
    "in",
    "the",
    "of",
    "or",
    "for",
    "a",
    "an",
    "and",
    "to",
    "on",
    "at"
]


class Title:
    """Generic handler for titles where all significant words should be capitalised.
    
    Take care, because not all titles need to be formatted this way. Some only need the first word to be capitalised.
    """
    
    def __init__(self, name: str):
        self.title = ""
        self.name = name
        
    def ask(self):
        """Asks for the title that needs to be formatted."""
        
        self.title = input(f"{self.name} title: ")
        
    @property
    def ieee(self) -> str:
        """Generates the title of the source in the proper format.
        
        IEEE dictates that all words in the title should be capitalised, except for insignificant words.
        There is no official list of insignificant words, so I made my own.
        
        This also abbreviates common words, the list is taken from the IEEE Reference Guide.
        """
        
        # Split up into a list of words so we can work with them individually
        words = self.title.split(" ")
        
        # First word is ALWAYS capitalised, even if insignificant - that's just standard grammar
        out = words[0].capitalize()
        
        # Capitalise the rest of the words, as long as they're significant
        for w in words[1:]:
            # Important to use w.lower(), or we might not always make a match when we should
            if w.lower() not in INSIGNIFICANT_WORDS:
                out += f" {w.capitalize()}"
                
            # If one of common abbreviations, use that instead
            elif w.lower() in COMMON_ABBREVS:
                out += f" {COMMON_ABBREVS[w].capitalize()}."
            
            # Again, we use w.lower() to make sure it's the correct case in the output
            else:
                out += f" {w.lower()}"
                
        # TODO: remove any ending punctuation
        
        return out
        