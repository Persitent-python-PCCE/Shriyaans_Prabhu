import re
txt="Contact us at 9876543210 or 987-654-3210. You can also call (987) 654-3210 or 987 654 3210 for support."
m=re.sub(r"(?:\(\d{3}\)|\d{3})[- ]?\d{3}[- ]?(\d{4})",r"******\1",txt)
print(m)