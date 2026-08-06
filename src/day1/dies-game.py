import random as r
ls1=[1,2,3,4,5,6]
ls2=[1,2,3,4,5,6]
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
# print(d1,d2)
# print(d1+d2)
print(f"Welcome to the game!")
while True:
    sm1,sm2=0,0
    T=input("Player1 hello do you want to roll? (y/n)")
    if T.lower()=="y":
        d1=r.choice(ls1)
        d2=r.choice(ls2)
        sm1=d1+d2
    
    elif T.lower()=="n":
        print(f"Game END")
        break
    else:
        print("please enter(y/n)")
    T2=input("Player1 hello do you want to roll? (y/n)")
    if T2.lower()=="y":
        d1=r.choice(ls1)
        d2=r.choice(ls2)
        sm2=d1+d2
    elif T2.lower()=="n":
        print(f"Game END")
        break
    else:
        print("please enter(y/n)")
    if pds[sm1]<pds[sm2]:
         print(f"Player1 wins!!")
         print(f"sums: Player1={sm1} Player2={sm2}")
    elif pds[sm1]>pds[sm2]:
        print(f"Player2 wins!!")
        print(f"sums: Player1={sm1} Player2={sm2}")
    else:
        print(f"Draw!!")
        print(f"sums: Player1={sm1} Player2={sm2}")

    