#WAP TO REVERSE DIGITS

num=12345
n=num
rev=0

while n>0:
    last_digit=n%10 #EXTRACT DIGITS
    rev=rev*10+last_digit
    n//=10

print(rev)