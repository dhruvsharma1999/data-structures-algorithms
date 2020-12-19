#python implementation of delimiters for implementing application of stacks 
from arrayStack import Empty, AarrayStack

def is_matched(expr):
    """Returns True is all delimiters are properly match; False other wise"""
    lefty = "({["
    righty = ")}]"

    S = AarrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty() 
    