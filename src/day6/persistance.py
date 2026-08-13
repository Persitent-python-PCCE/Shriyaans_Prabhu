import pickle
import shelve
student=[{"id":101,"name":"Shriyaans","marks":[78,98,86]},{"id":102,"name":"Prakash","marks":[80,98,89]}]
with open("student.pkl","wb") as Of:
    pickle.dump(student,Of)
Of.close()
with open("student.pkl","rb") as Rf:
    st=pickle.load(Rf)
Rf.close()
print(st)
with shelve.open("data") as Op:
    Op["101"]={"name":"Shriyaans","Marks":80}
Op.close()
with shelve.open("data") as Op:
    print(Op["101"])
Op.close()