#WAP TO COUNT DIGITS

num=12345
n=num
count=0

while n>0:
    count+=1
    last_digit=n%10 #EXTRACT DIGITS
    n//=10

print(count)


