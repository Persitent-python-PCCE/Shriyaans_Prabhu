#Queue Implementation
class Stack:
    def __init__(self,sz):
        self.sz=sz
        self.s=[]
    def push(self,el):
        if len(self.s)==self.sz:
            print(f"Stack Full!")
        else:
            self.s.append(el)
    def pop(self):
        if self.s. is None:
            print("Stack Empty.")
        else:
            return self.s.pop()
    def top(self):
        if self.s is None:
            print("Stack Empty.")
        else:
            return self.s[-1]
# implementation of Queue
class Queue:
    def __init__(self,sz):
        self.sz=sz
        self.Q=[]
    def enqueue(self,el):
        if len(self.Q)==self.sz:
            print("Queue is Full")
        else:
            self.Q.append(el)
    def dequeue(self):
        if self.Q is None:
            print("Queue is Empty.")
        else:
            return self.Q.pop(0)
    def front(self):
        if self.Q is None:
            print("Queue is Empty.")
        else:
            return self.Q[0]
    def back(self):
        if self.Q is None:
            print("Queue is Empty.")
        else:
            return self.Q[-1]


            
