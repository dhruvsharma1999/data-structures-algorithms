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

21 ￼
B

22 ￼
C

21 Answer: B
 Listen from here  Locate  Explain  Report
22 Answer: C
 Listen from here  Locate  Explain  Report
Questions 23-24
Write the correct letters, A-E, next to questions 23-24.

Which TWO of the following are sales strategies for chocolate in Italy and Germany?

A Locate near a children’s school
B Change the location of the product on shelves
C Give a free gift
D Make it the cheapest brand
E Make Schmutzig the second cheapest brand
23-24 Answer: B,E
 Listen from here  Locate  Explain  Report
Questions 25-30
Complete the table below.

Write NO MORE THAN TWO WORDS for each answer.

Research plan

Betty is interested in how 25 ￼ affects the sales of cosmetics and 26 ￼

Bruce is going to be concerned with how 27 ￼ may impact on sales of cookies and the relationships among 28 ￼, 29 ￼, and sales.

The professor advised the students to bear in mind the extensions of 30 ￼

25 Answer: colour/color
 Listen from here  Locate  Explain  Report
26 Answer: cleaning products
 Listen from here  Locate  Explain  Report
27 Answer: (different) containers
 Listen from here  Locate  Explain  Report
28 Answer: materials
 Listen from here  Locate  Explain  Report
29 Answer: image
 Listen from here  Locate  Explain  Report
30 Answer: advertisement
 Listen from here  Locate  Explain  Report
Previous NextSECTION 3
Audio Player
￼
￼
00:00
29:53
￼Use Up/Down Arrow keys to increase or decrease volume.
Change Audio Sources 


SECTION 3
PROFESSOR: Come in!
BETTY: Professor Dundee? We’re ready to make our presentation.
PROFESSOR: Oh, yes. I did say one o’clock, didn’t I? Please, sit down. So, who goes first? Bruce? Or you, Betty?
BETTY: I guess I could. Bruce is always a little shy.

PROFESSOR: Not after he’s had a lager for lunch, eh Bruce? BRUCE: Heh, heh. No, Betty really should go first.

BETTY: OK. Well, I’m reporting on the effects of different marketing strategies on the cheese and oil markets. Different strategies obviously affect the sales volume differently. I looked at the sales in two countries, New Zealand and Colombia.
PROFESSOR: And what did you find, pray tell?
BETTY: Well, in New Zealand, the sales of both oil and cheese have declined pretty steadily. And in fact, the sales have decreased more quickly than the population. On the other hand, in Colombia, the volume of sales for both products has remained the same.
PROFESSOR: Wait, so you said sales in New Zealand have been going down?
BETTY: Correct. Suppliers have introduced two new upscale brands of each product, which are a bit expensive but very tasty. The big ad agencies are trying out a new series of ads that shift the focus from health to great taste. They think that will get sales moving up in New Zealand, where the population is less affluent and gen­erally less health-conscious.
PROFESSOR: Brilliant. Thank you. And Bruce?
BRUCE: Uhhh... yeah. My report is about chocolate sales in Italy and Germany. The two countries’ marketers have found out that you have to market chocolate differently in each country.
PROFESSOR: For example?
BRUCE: In Italy, “Kostig”, the most expensive brand, pays shop owners to put the candy just about knee-high for an adult.
PROFESSOR: I don't see...
BRUCE: For little kids, that’s about eye level! That bright red candy is the first one they see, so they buy it! Even better, they start telling their moms to buy it, too!
PROFESSOR: So, you mean...
BRUCE: Well, I mean, in Italy if you locate your product at the right location of shelves, sales do great. They say it doesn’t matter much what brand of chocolate you’re selling. As for Germany...
PROFESSOR: “Das Land der Schokolade”.

BRUCE: Huh?
PROFESSOR: That’s German. It means “The Land of Chocolate”. Germans love the stuff, so people make a joke and call Germany that.
BRUCE: Oh... uh, right...
PROFESSOR: So, you were saying?
BRUCE: Well, like you pointed out, Germans love chocolate. But they’re thrifty. For a long time, the biggest selling brand was “Schmutzig", mostly because it was the second cheapest, but didn’t taste too bad.

PROFESSOR: Again brilliant! A pretty good job, both of you. Tell me,
what do you plan to investigate next week?
BETTY: I’m especially interested in the effects of colour on sales of products, so I’ll be looking at ads for cosmetics and cleaning products in the local market. You know, like the distinct orange colour of Mr. Muscle, lavatory cleaning products.
BRUCE: And you, Bruce?
I'm focusing on the effects of different containers on sales of cookies. So I’m going to look into packaging for cookies and how the materials they use will affect the image, and in turn sales. You know, most containers are paper, but some expensive cookies come in metal boxes. The shiny metal boxes catch people’s attention and the image remains in the memory longer.
PROFESSOR:Well, it sounds like you two are all set. But as always in this course, I urge you both to pay much more attention to the advertisement extensions. That’s often the key. Alright, any questions for me before you go.
BRUCE: No, I think I’m all set. Thanks!
Me too. Thanks, Professor Dundee. See ya later.


    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
