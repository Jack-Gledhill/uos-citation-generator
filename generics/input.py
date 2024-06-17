# Responses that are clearly a YES
YES_RESPONSES: list[str] = [
    "yes",
    "y",
    "true",
    "t",
    "1"
]

# Responses that clearly mean NO
NO_RESPONSES: list[str] = [
    "no",
    "n",
    "false",
    "f",
    "0"
]


def input_bool(message: str) -> bool:
    """A simple handler for making yes/no requests via the terminal.
    
    This function isn't biased, i.e. if a nonsense reply is given, it errors instead of defaulting to true or false.
    """
    
    raw = input(f"{message} [Y/N]: ")
    if raw.lower() in YES_RESPONSES:
        return True
    
    elif raw.lower() in NO_RESPONSES:
        return False
    
    else:
        raise IOError("invalid y/n answer")
    