# wap to find a strong number(krisnamurthy num)
# ---------------------------------------------------------------------------------------------------------
n=int(input("enter a num:"))
temp=n
i=1
sum=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact 
    n=n//10
if sum==temp:
        print(temp,"is a strong num")
else:
        print("nopp its not a strong num")
