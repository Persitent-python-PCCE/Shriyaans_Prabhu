class PC:
    # Global variable
    __counter=0
    def __init__(self,Screen,CPU,GPU):
        self.Screen=Screen
        self.CPU=CPU
        self.GPU=GPU
        PC.__counter+=1
    def __str__(self) -> str:
        return f"{PC.__counter}"
    def details(self):
        print(f"Screen:{self.Screen}")
        print(f"CPU:{self.CPU}")
        print(f"GPU:{self.GPU}")
    def __str__(self):
        return f"Screen:{self.Screen} CPU:{self.CPU} GPU:{self.GPU}"
Ob=PC("OLED","Intel i7","Xe Graphics")
Ob1=PC("OLED","Intel i5","Iris Xe Graphics")
Ob2=PC("IPS","AMD Ryzen 5","Radeon Graphics")
Ob3=PC("AMOLED","Intel i9","UHD Graphics")
Ob4=PC("LCD","AMD Ryzen 7","Radeon 780M")
# Ob.details()
print(Ob)
class Dell(PC):
    __counter=0
    def __init__(self,version,price,Screen,CPU,GPU):
        super().__init__(Screen,CPU,GPU)
        self.version=version
        self.price=price
        Dell.__counter+=1
    def __str__(self) -> str:
        return f"{Dell.__counter}"
    def show(self):
        print(f"Version:{self.version}")
        print(f"Price:{self.price}")
pc_ob=Dell("Hp Envy EVO",100000,"OLED","Intel i7","Xe Graphics")
pc_ob.details()
pc_ob.show()

print(pc_ob)