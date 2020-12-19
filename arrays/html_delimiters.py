#python program to match delimiter of HTML tags using stack LIFO property
from arrayStack import Empty, AarrayStack

def is_matched_html(raw):
    """Return True if all HTML tags are matched properly and False otherwise"""
    S = AarrayStack()

    #we input HTML as a raw string 
    j = raw.find('<')
    # .find() finds the first occurance of the specified value
    # .find() retunrs -1 if the value specified is not found
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]

        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()