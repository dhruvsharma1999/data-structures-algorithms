#pyhton 3 program to implement simple balanced parentheses using stacks
#stack class 

class Stack:

    #stack constructor
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []
    
    def push(self, item):
        return self.item.append(item)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[len(self.item -1)]
     
    #implementing balanced parantheses function
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0 

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol  == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('((()))))'))
