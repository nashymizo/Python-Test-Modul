import hashlib

# 1. Unser Start-Text (das könnten später Funktionsname + Parameter sein)
mein_text = "addiere_4_3"

# 2. WICHTIG: Der MD5-Fleischwolf schluckt keinen normalen Text (Strings),
# sondern nur Datenpakete ("Bytes"). Wir müssen den Text also kurz umwandeln:
text_als_bytes = mein_text.encode('utf-8')

# 3. Jetzt werfen wir die Bytes in den MD5-Algorithmus
hash_objekt = hashlib.md5(text_als_bytes)

# 4. Mit .hexdigest() holen wir uns den fertigen, lesbaren 32-Zeichen-Hash heraus
fertiger_hash = hash_objekt.hexdigest()

print(f"Original: {mein_text}")
print(f"Hash:     {fertiger_hash}")
print(hash_objekt)