def fact_sum(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s
n=int(input())
m=int(input())
a=fact_sum(n)
b=fact_sum(m)
if a==m and b==n:
    print('Amicable')
else:
    print('Not Amicable')