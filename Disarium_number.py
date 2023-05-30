n=int(input())
l = list(str(n))
s=0
for i in range(len(l)):
    s+=int(l[i])**(i+1)
if s==n:
    print(True)
else:
    print(False)