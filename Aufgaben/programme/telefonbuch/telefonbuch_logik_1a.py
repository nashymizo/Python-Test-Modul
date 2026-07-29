import re

def pruefe_text(text : str) -> bool:

    pattern = r"^[a-zA-Z0-9äöüÄÖÜß ]{1,32}$"
    return bool(re.match(pattern, text))



def pruefe_nummer(nummer : str) -> bool:

    pattern = r"^\d+ / \d+$"
    return bool(re.match(pattern, nummer))

