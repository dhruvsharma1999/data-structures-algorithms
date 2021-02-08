"""
Create a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
Create an integer, , and initialize it to .
There are  types of queries:
Query: 1 x y
Find the list within  at index .
Append the integer  to the .
Query: 2 x y
Find the list within  at index .
Find the value of element  where  is the number of elements in lastAnswer$.
Print the new value of  on a new line
Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.

Function Description

Complete the dynamicArray function below.

dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in 
- string queries[q]: an array of query strings

Returns

int[]: the results of each type 2 query in the order they are presented
Input Format

The first line contains two space-separated integers, , the size of  to create, and , the number of queries, respectively.
Each of the  subsequent lines contains a query in the format defined above, .

Constraints

It is guaranteed that query type  will never query an empty array or index.
Sample Input

2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
Sample Output

7
3
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)]
    lastAnswer = 0
    result = []
    #query type one 
    for q in queries:
        if q[0] == 1:
            seq=(q[1] ^ lastAnswer) %n
            arr[seq].append(q[2])
            
        else:
            seq=(q[1] ^ lastAnswer) %n
            lastAnswer = arr[seq][q[2]%len(arr[seq])]
            result.append(lastAnswer)
    return result
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
