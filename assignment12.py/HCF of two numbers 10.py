'''10. Write a python script to calculate HCF of two numbers'''
  
print("enter a two number")
a,b=int(input()),int(input())
while a%b!=0:
    rem=a%b
    a=b
    b=rem
print("hcf is",b)
