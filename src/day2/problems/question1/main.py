from log_utils import read_logs as Reader
import collections 
from collections import Counter
LOGS=Reader("app.log")
cl=[]
print("==Log Summary==")
for L in LOGS:
    cl.append(L[0])
C=dict(Counter(cl))
for i in C:
    print(f"{i}:{C[i]}")
for L in LOGS:
    if L[0]=="ERROR":
        print(f"- {L[1]}")
with open("log_summary.txt.","w") as log_sm:
    log_sm.write("    ==Log Summary==     \n")
    for i in C:
        log_sm.write(f"        {i}:{C[i]}\n       ")
 
    log_sm.write(f"   Error Found:\n   ")
    for L in LOGS:
        if L[0]=="ERROR":
            log_sm.write(f"-{L[1]}\n")

    