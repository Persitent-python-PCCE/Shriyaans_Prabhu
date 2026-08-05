# Key Word arguments
def student(**data):
    print(data)
student(name="Shriyaans",age=22,city="Ponda")
def agg(*nums):
    return sum(nums)
print(agg(1,2,2))
# multiple returns
def maths_op(a,b):
    """a return math based function which returns multiple values """
    return a+b,a-b,a*b,a//b
t=maths_op(4,2)
print(t)
# function nesting and local varialbe scope 
def out():
    name=input("enter user name:")
    def inner():
        name="localhost"
        print(f"user:{name}")
    print(f"{name}")
# lamada function anonymous
cube=lambda c:c*c*c
print(cube(2))
comp=lambda a,b: a if a>b else b
print(comp(1,90))
ls=[1,2,3,4]
ls2=[2,1,2,1]
# map and filter 
res=map(cube,ls)
print(list(res))
res2=map(lambda a,b: a*b,ls,ls2)
print(list(res2))
cond=filter(lambda c: c%2==0,ls2)
print(list(cond))