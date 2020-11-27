#binary seacrch algorithm in python 3

def binary_search(llist, item):
    """
    Take a sorted list as input.

    Returns the item's index """
    
    low = 0 
    high = len(llist) - 1

    while low < = high:
        mid = (low + high) / 2
        guess = llist[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
        
        return None

