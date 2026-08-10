from abc import ABC,abstractclassmethod
# hidden methods / abstract methods ->only decl , no def 
# import ABS from abc
# cannot create an object 
# cannot instatiate
class Bank(ABC):
    def __init__(self,name,manager,location):
        self.name=name
        self.manager=manager
        self.location=location
    @abstractclassmethod
    def payment(self):
        pass
    def info_display(self):
        print(f"Bank Info: {self.name} {self.location}")
# must overrride all parent abstract methods
class Customer(Bank):
    def __init__(self, name, manager, location):
        super().__init__(name, manager, location)
    def payment(self):
        return f"UPI Payment Done."
c=Customer("HDFC","Mohan","Ponda")
print(c.payment())