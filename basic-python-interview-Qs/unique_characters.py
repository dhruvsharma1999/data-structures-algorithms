"""
Implement an algorithm to determine if a string has all unique character"""

"""
This problem can be solved by using the set() function of python, which returns all the uniqueue elements of the string"""

def is_unique(s):
    return len(s) == len(set(s))



print(is_unique("sat"))