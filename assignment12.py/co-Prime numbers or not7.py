'''7. Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.
'''


from fractions import gcd
num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))
if gcd(num1,num2)==1:
    print(num1,"and",num2,"co_prime")
else:
    print(num1,"and",num2,"not co_prime")