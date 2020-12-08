#python program for implementing selection sort

import sys
A= [64, 25, 12, 22, 11]

#traverese through all the elements of array
for i in range(len(A)):

    #find the minimum element in the remaining unsorted array
    min_index = i
    for j in range(i+1, len(A)):
        if A[min_index] > A[j]:
            min_index = j

    # swap the found minimum element
    # with the first element
    A[i], A[min_index] = A[min_index], A[i]


print("Sorted array")
for i in range(len(A)):
    print(A[i])
