"""
GIven two strings, write a function to decide if one is a permutation
of the other """

str_1 = "coding bootcamp"
str_2 = "codignboootcapm"

def is_permutation(s1, s2):
    s1 = s1.replace(" ", "")
    s2 = s2.replace(" ", "")

    if len(s1) != len(s2):
        return False

    for c in s1:
        if c in s2:
            s2 = s2.replace(c, "")

    return len(s2) == 0


print(is_permutation(str_1,str_2))