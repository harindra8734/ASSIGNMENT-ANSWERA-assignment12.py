'''4. Write a python script to print all Prime numbers between two given numbers (both
values inclusive)
'''

lower=int(input("enter lower number range:"))
upper=int(input("enter upper number range:"))
for num in range(lower,upper+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
         count+=1
    if count==2:
        print(num)
 

