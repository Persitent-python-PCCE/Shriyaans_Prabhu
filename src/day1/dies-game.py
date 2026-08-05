import random as r
ls1=[1,2,3,4,5,6]
ls2=[1,2,3,4,5,6]
d1=r.choices(ls1)
d2=r.choices(ls2)
outcomes=[]
for i in ls1:
    for j in ls2:
        outcomes.append((i,j))
# print(outcomes)
summ=[]
for i in ls1:
    for j in ls2:
        summ.append(i+j)
# print(summ)
pds={}
for i in summ:
    pds[i]=summ.count(i)/36
# print(pds)
print(d1,d2)