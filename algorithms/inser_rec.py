# Insertion sort algorithm applied recursively
#
def insertionSortRecursive(arr, n):
    #base case
    if n < 1:
        return

    #sort first n-1 elements
    insertionSortRecursive(arr, n-1)

    last = arr[n-1]
    ## need to breakdown the working first...continued

