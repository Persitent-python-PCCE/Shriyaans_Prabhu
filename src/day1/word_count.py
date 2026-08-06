st= "Hello world"
words=st.split(" ")
count=0
for word in words:
    if word in "Hello":
        print("True")
    count+=1
print(f"total words:{count}")