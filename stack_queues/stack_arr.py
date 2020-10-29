#python program for implementation of stack 
#this program use array for implementing stacks 

#stack class 
class Stack:
    def __init__(self): #constructor of stack class
        self.item = []

    #method to check is stack is empty or not, returns a boolean
    def isEmpty(self):
        return self.item == []

    #method to push item to the top of the stack
    def push(self, item):
        self.item.append(item)

    #method to pop an item from the top of the stack
    def pop(self):
        return self.item.pop()

    #to look at the items in stack
    def peek(self):
        return self.item[len(self.item)-1]
    
    #method to return the size of the stack
    def size(self):
        return len(self.item)

#implementing stack 

s = Stack()

print(s.isEmpty())
s.push(4)
s.push("dog")
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
