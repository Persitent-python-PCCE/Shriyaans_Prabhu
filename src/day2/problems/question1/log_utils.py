def parse_line(line):
    part=line.split()
    level=part[2]
    message=" ".join(part[3:])
    # print(level,message)
    return level,message
def read_logs(path):
    entires=[]
    with open(path,"r") as Of:
        for line in Of:
            entires.append(parse_line(line))
    return entires
 
