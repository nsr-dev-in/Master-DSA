#WAP TO CHECK PRIME NO.
from math import sqrt

num=3
n=num

count=0

for i in range(1,int(sqrt(n)+1)):
    if n%i==0:
        count+=1
        if n//i!=i:
            count+=1

if count==2:
    print("PRIME")
else:
    print("NOT PRIME")