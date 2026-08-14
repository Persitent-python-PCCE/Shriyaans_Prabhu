import re
code=input("Enter a code:").strip()
mtch=re.fullmatch(r"^[A-Z]{2,3}-\d{4}[A-Z]?$",code)
if mtch:
    print(f"Valid")
else:
    print(f"Invalid")
