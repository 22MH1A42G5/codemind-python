def divide(n):
    for i in n:
        i=int(i)
        n=int(n)
        if i==0:
            return False
        if n%i!=0:
            return False
    return True
a=int(input())
b=int(input())
for i in range(a,b+1):
    i=str(i)
    if divide(i):
        print(i,end=" ")