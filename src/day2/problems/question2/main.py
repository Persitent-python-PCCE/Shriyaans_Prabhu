import re
from redaction_config import SENSITIVE as S
def redication_config(path):
    count={}
    with open(path,"r") as Of:
        text=Of.read()
        for word in S:
            text,ct=re.subn(word,"[REDACTED]",text,flags=re.IGNORECASE)
            count[word]=ct
        print(f"{text}")
    with open("report_redacted.txt","w") as Wf:
        Wf.write("-- report_redacted.txt --\n")
        Wf.write(text)
        Wf.write("\n-- console --\n")
        Wf.write("Redaction complete.\n")
        Wf.write(f" {S[0]}-> {count["Titan"]} occurrences \n")
        Wf.write(f"{S[1]} -> {count["Acme Corp"]} occurrences redacted\n")
        Wf.write(f"Output saved to report_redacted.txt\n")
redication_config("report.txt")
