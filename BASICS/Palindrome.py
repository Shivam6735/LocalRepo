n=123454321
num= n
result = 0
while num>0:
    id = num%10
    result = (result*10)+id
    num=num//10
if result==n:
    print("It is a Palindrome")
else:
    print("It's not a Palindrome")