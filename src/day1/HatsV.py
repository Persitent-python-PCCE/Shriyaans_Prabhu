name=input("Enter student name:")
signal=input("signal:")
def student(n,sig):
    G,H,R,S=0,0,0,0
    for l in sig:
        if l in "Gg":
            G +=1
        elif l in "Hh":
            H +=1
        elif l in "Rr":
            R +=1
        elif l in "Ss":
            S+=1
    if G>H and G>R and G>S:
        print(f"{name} you belong in Gryffindor ({G} Signals)")
    elif H>G and H>R and H>S:
        print(f"{name} you belong in Hufflepuff ({H} Signals)")
    elif R>G and R>H and R>S:
        print(f"{name} you belong in Ravenclaw ({R} Signals)")
    elif S>G and S>H and S>R:
        print(f"{name} you belong in Slytherin ({S} Signals)")

student(name,signal)