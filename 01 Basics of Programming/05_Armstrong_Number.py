#WAP TO CHECK ARMSTRONG NUMBER

num=153
n=num
check=0

while n>0:
    last_digit=n%10 #EXTRACT DIGITS
    check=check+last_digit**3
    n//=10 #REMOVE LAST DIGIT

if check==num:
    print("True")
else:
    print("False")