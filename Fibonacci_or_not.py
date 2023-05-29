def fib(n):
    if n==0 or n==1:
        return 1
    c=0
    d=1
    e=c+d
    while True:
        e=c+d
        c,d=d,e
        if e==n:
            return 1
        elif e>n:
            return 0
n=int(input())
if fib(n)==1:
    print(True)
else:
    print(False)