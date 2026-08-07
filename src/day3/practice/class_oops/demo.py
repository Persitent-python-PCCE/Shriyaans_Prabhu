class Car:
    count_inatance=0
    def __init__(self,name,brand,price,milage):
        self.name=name
        self.brand=brand
        self.price=price
        self.milage=milage
        Car.count_inatance+=1
    def details(self):
        print(f"Name Brand Price Milage")
        print(f"{self.name} {self.brand} {self.price} {self.milage}")
    def price_difference(self):
        on_road_price=self.price+120000+(self.price*0.05)
        print(f" On Road Price:{on_road_price}")
    @staticmethod
    def color(color):
        print(f"color is :{color}")

    
c=Car("Innova Hycross","Toyota",40000000,"12km/l")
c2=Car("Fortuner","Toyota",50000000,"9km/l")
c.details()
c.price_difference()
c.color("Purple")

c2.details()
c2.price_difference()
c2.color("white")
print(c.count_inatance)