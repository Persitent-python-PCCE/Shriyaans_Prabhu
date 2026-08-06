def redication_config(path):
    ls=[]
    txt=[]
    ct,ap=0,0
    final_message=None
    Acme_Corp="Acme Corp"
    Titan="Titan"
    with open(path,"r") as Of:
        for line in Of:
            ap+=line.count("Acme Corp")
            ct+=line.count("Titan")
            line = line.replace("Acme Corp","[REDACTED]")
            line =line.replace("Titan","[REDACTED]")
            txt.append(line)
        final_message=" ".join(txt)
    print("-- report_redacted.txt --")
    print(final_message)
    print("-- console --")
    print("Redaction complete.")
    print(f"Titan -> {ct} occurrences ")
    print(f"Acme Corp -> {ap} occurrences redacted")
    print(f"Output saved to report_redacted.txt")
    with open("report_redacted.txt","w") as Wf:
        Wf.write("-- report_redacted.txt --\n")
        Wf.write(final_message)
        Wf.write("\n-- console --\n")
        Wf.write("Redaction complete.\n")
        Wf.write(f"Titan -> {ct} occurrences \n")
        Wf.write(f"Acme Corp -> {ap} occurrences redacted\n")
        Wf.write(f"Output saved to report_redacted.txt\n")
# redication_config("report.txt")