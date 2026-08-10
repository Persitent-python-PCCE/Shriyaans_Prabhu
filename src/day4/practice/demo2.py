class Number:
    counter=0
    @classmethod
    def count(cls,counter):
        cls.counter+=1
        print(f"{cls.counter}")
    # @classmethod
    # def 
    @staticmethod
    def number(num):
        return num
    def __init__(self,value):
        self.value=value
    def __add__(self,other):
        if isinstance(other,Number):
            return Number(self.value+other.value)
        else:
            return NotImplemented
    def __mul__(self, other):
        return Number(self.value*other.value)
    # def __str__(self):
    #     return f"Value: {self.value}"
    def __repr__(self):
        return f"Value: {self.value}"
n1=Number(1)
n2=Number(4)
res=n1+n2
print(res.value)
print(n2)
print(repr(n2))
n2.count(2)
print(f"{n1.number(30)}")