import re

text = "Artikel A1234 kostet 49 Euro und Artikel B456 kostet 99 Euro"

print(re.search("Hello World", text))

print(re.findall(r"[0-9]+", text))

print(re.findall(r"[A-Z][0-9]+", text))

#anfänger
print(text[:29])
print(text[-27:])
#profi
print(re.findall(r"[A-Z][0-9]+", text))
print(re.findall(r" ([0-9+]+)", text))