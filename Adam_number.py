n=int(input())
m=int(str(n)[::-1])
n=n**2
m=m**2
m=int(str(m)[::-1])
if m==n:
    print(True)
else:
    print(False)