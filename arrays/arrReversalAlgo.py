#python program for reversal algorithm of array rotation
#function to reverse arr[] from index start to end

def reverseArray(arr, start, end):
    while(start < end):

        
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1



#function to left rotate arr[] of size n by d
def leftRotate(arr, d):
    if d ==0:
        return
    n = len(arr)
    #in case rotating factor is greater than array
    d = d%n

    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)

#function to print an array
def printArray(arr):
    for i in range(0,len(arr)):
        print(arr[i])

arr = [1,2,3,4,5,6,7]
n = len(arr)
d = 2

leftRotate(arr, d) # rotate array by 2
printArray(arr)





