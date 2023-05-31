def prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return False
    return True
p=1
np=1
n=int(input())
lst=list(map(int,input().split()))
for i in lst:
    if prime(i):
        p=p*i
    else:
        np=np*i
print(abs(p-np))