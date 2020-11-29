#python program to calculate disk usage - example of recursion

import os #importing os module to interact with the os

def disk_usage(path):
    """Returns the number of bytes by a file/folder and any descendents"""
    total = os.path.getsize(path)           #directory usage
    if os.path.isdir(path):                 #if this is a directory
        for filename in os.listdir(path)    #then for each child
        childpath = os.path.join(path, filename) 
        childpath += disk_usage(childpath)  #add child's usage to total 

    print('{0:<7}'.format(total), path)
    return total


disk_usage('/home/Desktop/')
