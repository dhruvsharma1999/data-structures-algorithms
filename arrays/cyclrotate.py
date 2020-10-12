#Python3 code to cyclically rotate an array by one

#function for rotation
def rotate(arr, n):
    temp = arr[n-1]
    for i in range(n-1, 0, -1):#going backwards from n-1 to 0
        arr[i] = arr[i-1]

    arr[0] = temp
        

#driver function
arr = [1,2,3,4,5,]
n = len(arr)
for i in range(0,n):
    print(arr[i], end =' ')

rotate(arr, n)

#printing reversed array 
print("\nRotated array is")
for i in range(0, n):
    print (arr[i], end=' ')
    
print("\r")    
