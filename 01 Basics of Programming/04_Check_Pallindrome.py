#WAP TO CHECK PALLINDROME NUMBER

num=12345
n=num
rev=0

while n>0:
    last_digit=n%10 #EXTRACT DIGITS
    rev=rev*10+last_digit
    n//=10

if rev==num:
    print("True")
else:
    print("False")