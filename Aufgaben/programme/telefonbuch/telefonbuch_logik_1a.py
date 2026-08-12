import re

def pruefe_text(text : str) -> bool:

    pattern = r"^[a-zA-ZäöüÄÖÜß ]{1,32}$"
    return bool(re.match(pattern, text))



def pruefe_nummer(nummer : str) -> bool:

    pattern = r"^\d+ / \d+$"
    return bool(re.match(pattern, nummer))

