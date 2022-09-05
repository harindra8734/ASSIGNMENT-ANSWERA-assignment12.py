'''2. Write a python script to check whether a given number is Prime or not'''


n=int(input("enter a number"))
temp=0
for i in range(2,n):
    if n%i==0:
        print("number is not prime")
        break
if temp==0:
    print("number is prime")
