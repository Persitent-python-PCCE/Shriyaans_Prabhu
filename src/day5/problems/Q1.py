import json
import random
import datetime as dt
class student_list:
    def __init__(self,number,y):
        self.number=number
        self.year=dt.date(year=y,month=1,day=2)
        self.lst_name=["Kumar","Raj","Amit","Priya","Riya"]
        self.lst_dept=0
        self.student_lst=[]
        self.age=0
        self.marks1=0
        self.marks2=0
        self.marks3=0
        self.p_count=0
        self.f_count=0
        self.average=0
        self.avg_lst=[]
    def return_student_list(self):
        total,avg=0,0
        status=None
        for i in range(1,(self.number+1)):
            if self.number>5:
                print("max 5 limit!")
                break
            name=random.choice(self.lst_name)
            self.lst_dept=random.choice(["Computer Science","Information Technology","Electronics","Mechanical"])
            self.marks1=random.randint(0,100)
            self.marks2=random.randint(0,100)
            self.marks3=random.randint(0,100)
            self.age=random.randint(18,25)
            total=self.marks1+self.marks2+self.marks3
            avg=total/3
            self.average=avg
            if self.marks1<40 or self.marks2<40 or self.marks3<40:
                status="Fail"
                self.f_count+=1
            else:
                status="Pass"
                self.p_count+=1
            self.student_lst.append({"student_id":i,"name":name,"age":self.age,"department":self.lst_dept,"marks":{"python":self.marks1,"database":self.marks2,"networks":self.marks3},"total":total,"average":avg,"result":status,"exam_date":self.year.isoformat()})
            self.avg_lst.append(self.average)
            self.lst_name.remove(name)
            self.year=self.year+dt.timedelta(days=5)
    def return_list(self):
        return self.student_lst
    
    def results(self):
        self.return_student_list()
        print("Student Performance Summary")
        print("----------------------------")
        print(f"Total Students : {self.number}")
        print(f"Passed : {self.p_count}")
        print(f"Failed : {self.f_count}")
        print(f"Highest Average :{max(self.avg_lst)}")
        print(f"Lowest Average : {min(self.avg_lst)}")
        with open("student_info.json","w") as Of:
            json.dump(self.return_list(),Of,indent=2)
        
ob=student_list(5,2026)
ob.results()



        

    
