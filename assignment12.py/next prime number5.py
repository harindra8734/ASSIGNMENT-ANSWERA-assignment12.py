'''5. Write a python script to find next prime number of a given number'''


n=int(input("enter a number"))
k=n+1
while k:
    for i in range(2,k):
        if k%i==0:
            break
    if i==k:
        print(k,"next prime number",n)
    else:
        k+=1