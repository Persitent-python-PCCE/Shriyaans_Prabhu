teams=[("Brazil", 3, 0, 0), ("Japan", 1, 2,
0), ("Spain", 2, 0, 1), ("Ghana", 0, 1,
2)]
fl=list(filter(lambda FL: (FL[1]*3)>=6  and FL[3]<=1,teams))
# print(fl)
print("Advancing to knockout:")
for i in fl:
    print(f"{i[0]} - {i[1]*3} pts")

