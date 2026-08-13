import os
import sys # python interpreter
import datetime as dt
from dotenv import load_dotenv
import glob as G
import random 
load_dotenv()
print(os.getenv("USER_NAME"))
print(sys.version)
print(sys.argv)
print()
# datetime modules
n=dt.datetime.now()
print(n)
# print(n.second)
date_string="12-08-2026 10:50:35"
print(n.strftime("%D %m %Y %B %A"))
d=dt.date(year=2026,month=10,day=23)
print(d)
#timedelta
today=dt.date.today()
future=today+dt.timedelta(days=5)
print(future)
print(G.glob("okey.py"))
print(G.glob("../file?.txt"))
print(random.randint(1,10))
print(random.uniform(10,40))
# print(random.random)
print(random.choice(['shriyaans',"Prabhu","Prakash"]))
print(random.sample(['shriyaans',"Prabhu","Prakash"],k=2))