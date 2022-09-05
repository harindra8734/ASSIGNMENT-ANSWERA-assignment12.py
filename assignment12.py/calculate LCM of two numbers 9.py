'''9. Write a python script to calculate LCM of two numbers
'''
def computer_lcm(n1,n2):
    if n1>n2:
        higher=n1
    else:
        higher=n2
    value=higher
    while True:
        if higher%n1==0 and higher%n2==0:
            print("lcm is",n1,"and",n2,"is",higher)
            break
        else:
            higher=higher+value
print("enter the two number")
n1,n2=int(input()),int(input())
computer_lcm(n1,n2)

