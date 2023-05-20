def prime(n):
    k=int(n**0.5+1)
    for i in range(2,k):
        if(n%i==0):
            return False
    return True
p=0
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i) and i!=1:
        p=p+1
print(p)