"""
given astring, write a function to determine if it is a palindrome"""

import string #python STL, for removing punctuations from a string

def is_palindrome(s):
    """
    function to check if a string is palindrom or not 
    Returns a boolean value
    """
    s = s.lower() #convert the whole string into lowercase letters
    s = s.translate(None, string.punctuation) #removes pucntuation from the string, is there is any
    s = s.replace(" ", "") #Removes whitespaces from a string

    return s == s[::-1] #list splicing method to reverse a string 



str_1 = "race car"

print(is_palindrome(str_1))