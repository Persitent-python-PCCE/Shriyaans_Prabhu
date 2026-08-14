import re
s="Hello whorld "
print(f"{re.findall(r"Hello",s)}")
print(f"{re.search(r"3\.1","3.1122")}")
print(f"{re.findall(r"h.t","hat aeroplane hit apple banana hut")}")
print(f"{re.findall(r"^cat","catalog products")}")
print(f"{re.findall(r"ab*c","ab ac abc abbbbbbc")}")
print(f"{re.findall(r"colou?r","color colour")}")
print(f"{re.findall(r"\d{1,4}","1234 44443 122")}")
print(f"{re.findall(r"cat | dog","cat dog bird catdog dog cat ")}")
print(f"{re.findall(r"[aeiouAEIOU]","ab ac abc abbbbbbc")}")
print(f"{re.findall(r"[a-zA-Z]","aueoAOi123wkl")}")
print(f"{re.match(r"Hello","Hello world ")}")
print(f"{re.search(r"world","world").span()}")
print(f"{re.findall(r"\$\d+","The prices are $30,$40, $500")}")
d="I like cars and cars are cool."
num="numbers: 5, 10, 50, 90"
print(re.sub(r"cars","bikes",d,flags=re.IGNORECASE))
def num_op(match):
    return str(int(match.group())*2)
print(re.sub(r"\d+",num_op,num))
pattern=re.compile(r"\d+")
txt1="There are 12 cars"
txt2="bip 200, torque 250"
print(pattern.findall(txt1))
print(pattern.findall(txt2))
dob="Bor on 2004-01-23"
m=re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})",dob)
print(m.group("year"))
full_name="Shriyaans    Prabhu"
print(re.sub("\s+"," ",full_name))