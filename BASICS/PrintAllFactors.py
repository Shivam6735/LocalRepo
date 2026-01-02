# n = int(input("Enter a number : "))
# result = []
# for i in range(1,n+1):
#     if n % i ==0:
#         result.append(i)
# print(result)






# Better Solution

# n = int(input("Enter a number : "))
# result = []
# for i in range(1,n//2):
#     if n % i ==0:
#         result.append(i)
# result.append(n)
# print(result)








# OPTIMAL SOLUTION

from math import sqrt
n = int(input("Enter a number : "))
result = []
for i in range(1,int(sqrt(n))+1):
    if n % i ==0:
        result.append(i)
    if n//i != i:
        result.append(n//i)
print(result)
m = sorted(result)
print (m)




    

