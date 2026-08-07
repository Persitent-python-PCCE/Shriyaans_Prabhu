x=100
class MyException(Exception):
    pass
lst=[1,2,3,4,4,5,5,5,55,5,5,7]
while True:
    try:
        n=int(input("Enter a number:"))
        out=x/n
        if n>9999:
            raise Exception("Number greater than 5 digits.")
        print(round(x/n,2))
        print(lst[(x//n)])
    except ValueError as v:
        print(f"Value Error. {v}")
    except ZeroDivisionError as z:
        print(f"Not divsible by zero {z}")
    except (TypeError,ZeroDivisionError,ValueError):
        print("Multiple error")
    except IndexError as I:
        print(I)
    except Exception as e:
            print(e)
    except:
        print(f"Unknown Error.")
        break
    else:
        print(f" No Exception .")
    finally:
        print("End ")