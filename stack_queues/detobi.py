#program to convert decimat number to binary by using
# divide by 2 algorithm
#

from pythonds.basic import Stack

#function to divide by 2 and store the remainder in stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))

