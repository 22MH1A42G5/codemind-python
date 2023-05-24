def fact(n):
    p=1
    while(n!=0):
        p=p*n
        n=n-1
    return p
n=int(input())
t=n
s=0
while n!=0:
    r=n%10
    s=s+fact(r)
    n=n//10
if t==s:
    print('The number',t,'is a strong number')
else:
    print('The number',t,'is not a strong number')
    