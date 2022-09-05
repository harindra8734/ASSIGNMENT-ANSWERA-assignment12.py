'''3. Write a python script to print all Prime numbers under 100'''


for i in range(1,100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=' ')
    
      
    