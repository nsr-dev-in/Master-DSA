#WAP TO EXTRACT DIGITS

num=12345
n=num

while n>0:
    last_digit=n%10 #EXTRACT DIGITS
    print(last_digit,end=" ")
    n//=10

