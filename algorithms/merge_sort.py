#implementing merge sort 
import sys 

#fucntion for user to pass in list
def merge_sort(A):
    #function to extract starting and ending index of the list
    merge_sort_2(A, 0, len(A)-1)


def merge_sort_2(A, first, last):
    if first < last:
        middle = (first + last) // 2
        merge_sort_2(A, first, middle)
        merge_sort_2(A, middle+1, last)
        merge(A, first, middle, last)

def merge(A, first, middle, last):
    L = A[first:middle]
    R = A[middle:last+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range(first, last+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+= 1
        else:
            A[k] = R[j]
            j += 1


A = [5,9,33,5,7,8,2,5,7]
print(A)
merge_sort(A)
print(A)
