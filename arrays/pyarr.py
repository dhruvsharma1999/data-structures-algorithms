#python code to demonstrate the working of array
#array(), append(), insert()

import array # importing array module for array implementation

#initialize array with array values
#initialize array with signed intergers
arr = array.array('i', [1,2,3])

#printing the original array
print("The new created array is :" ,end=" ")
for i in range (0,3):
    print (arr[i], end=" ")

print("\r")

#using append() to insert new value at the end of the array
arr.append(4);

#printing appended array
print("The appended array is: ", end=" ")
for i in range (0,4):
    print(arr[i], end=" ")

print("\r")

#using insert() to insert value at specific position 
#insert 5 at 2nd position
arr.insert(2, 5)

#printing array after insertion
print("The array after insertion is: ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")

#using pop() to remove element at 2nd position
print("The popped element is: ",end=" ")
print(arr.pop(2));

#printing array afer popping.
print("The array after popping is: ", end=" ")
for i in range(0,4):
    print(arr[i], end=" ")

print("\r")

#using remove() to remove 1st occurance of 1
arr.remove(1);

#printing array after removing
print("The array after removing is: ", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")





















