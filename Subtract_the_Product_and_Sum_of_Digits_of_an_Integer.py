p=1
s=0
n=int(input())
t=n
while t!=0:
    r=t%10
    s=s+r
    t=t//10
while n!=0:
    r=n%10
    p=p*r
    n=n//10
print(p-s)