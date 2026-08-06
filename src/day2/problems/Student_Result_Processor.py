import csv
stundent_record=[]
count=0
g=0
student_results=[]
avg_sum=[]
passed,failed=0,0
with open("students.csv","r") as Of:
    record=csv.DictReader(Of)
    for line in record:
        stundent_record.append(line)
for student in stundent_record:
    roll_no=int(student["roll_no"])
    name=student["name"]
    maths=int(student["maths"])
    pyhsics=int(student["physics"])
    chemistry=int(student["chemistry"])
    t=maths+pyhsics+chemistry
    tv=t/3
    tv=round(tv,2)
    avg_sum.append(tv)
    if tv >=90:
        g="A"
        passed+=1
    elif tv>=75 and tv<=89:
        g="B"
        passed+=1
    elif tv>=60 and tv<=74:
        g="C"
        passed+=1
    elif tv>=40 and tv<=59:
        g="D"
        passed+=1
    elif tv <40:
        g="F"
        failed+=1
    student_results.append({"roll_no":roll_no,"name":name,"maths":maths,"physics":pyhsics,"chemistry":chemistry,"total":t,"average":tv,"grade":g})
    count+=1
# print(student_results)
print(f"-- students_result.csv --")
print(f"roll_no,name,maths,physics,chemistry,total,average,grade")
for L in student_results:
    print(L["roll_no"],L["name"],L["maths"],L["physics"],L["chemistry"],L["total"],L["average"],L["grade"])
print(f"-- console --")
print(f"Processed {count} students -> students_result.csv")
for t in student_results:
    if t["average"]==max(avg_sum):
        print(f"Class Topper : {t["name"]} (avg {t["average"]})")
print(f"Passed : {passed} | Failed : {failed}")
with open("students_result.csv","w") as Of:
    write=csv.writer(Of)
    write.writerow(["-- students_result.csv --"])
    write.writerow([f"roll_no,name,maths,physics,chemistry,total,average,grade"])
    for L in student_results:
        write.writerow([f"{L["roll_no"]},{L["name"]},{L["maths"]},{L["physics"]},{L["chemistry"]},{L["total"]},{L["average"]},{L["grade"]}"])
    write.writerow([f"-- console --"])
    write.writerow([f"Processed {count} students -> students_result.csv"])
    for t in student_results:
        if t["average"]==max(avg_sum):
            write.writerow([f"Class Topper : {t["name"]} (avg {t["average"]})"])
    write.writerow([f"Passed : {passed} | Failed : {failed}"])