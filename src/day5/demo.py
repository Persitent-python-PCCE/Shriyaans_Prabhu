import os # Operating System
import shutil # Shell utilities
import json 
print(os.getcwd())
# os.mkdir("logs")
# os.mkdir(r"C:/Users/Shriyaans/documents/work/Shriyaans_Prabhu/src/day5/logs")
exist=os.path.exists(r"C:/Users/Shriyaans/documents/work/Shriyaans_Prabhu/src/day5/logs")
try:
    os.makedirs("practice/codes",exist_ok=True)
    # os.rmdir("logs")
    # shutil.copy("./logs/logger.log","./day5/logger.log")
    # os.rename("./logs/app.log","./logs/logger.log")
    o=os.path.abspath("logs")
    os.path.basename(o)
    file="logger.log"
    name,extension=os.path.splitext(file)
    print(f"name:{name} Extension:{extension}")
except FileNotFoundError as E:
    print(E)
# os.chdir("../")
print(f"{os.listdir()}")