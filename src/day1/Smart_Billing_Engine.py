ls=[("Masala Chai", 3, 20), ("Samosa", 2,
15), ("Green Tea", 1, 30)]
r1=list(map(lambda Q: (Q[1]* Q[2]*1.05),ls))
print(r1)
print(sum(r1))