import timeit
def factorial(n):
    fact=1
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
def factorial_l(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    return fact
exc_time=timeit.timeit(lambda :factorial(50),number=100)
exc_time_loop=timeit.timeit(lambda : factorial_l(50),number=100)
print(exc_time)
print(exc_time_loop)