import re
txt="John Doe: 28, Alice Smith: 34, Bob: 19, Charlie Brown: 45"
nt=re.sub(r": "," - ",txt)
nt2=re.sub(r",","\n",nt)
print(nt2)
