#WAP TO PRINT ALL THE FACTORS OF A NUMBER

num=20

"""
#BRUTE FORCE
n=num
list=[]
for i in range(1,n+1):
    if n%i==0:
        list.append(i)
print(list)
"""


#OPTIMAL APPROACH
from math import sqrt
n=num
list=[]
for i in range(1,int(sqrt(n)+1)):
    if n%i==0:
        list.append(i)
        if n//i!=i:
            list.append(n//i)
print(list)

