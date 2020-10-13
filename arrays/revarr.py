#iterative python program to reverse an array

#function to reverse A[] from start to end

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end],A[start]
        start += 1
        end -= 1


#Driver function to test above case
A = [1,2,3,4,5,6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)
