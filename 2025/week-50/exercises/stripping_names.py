"""
Ανάθεσε σε μια μεταβλητή ένα όνομα με κενά μπροστά και πίσω.
Χρησιμοποίησε τις συναρτήσεις lstrip(), rstrip(), strip() και εκτύπωσε τα αποτελέσματα.
"""
name = "   Sofaki mou        "
name1 = "bb"
print(f"{name}{name1}")
print(f"{name.lstrip()}{name1}")
print(f"{name.rstrip()}{name1}")
print(f"{name.strip()}{name1}")
