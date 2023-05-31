n=int(input())
lst=list(map(int,input().split()))
x=0
for i in (0,int(n/2)):
    x=x+lst[i]
y=sum(lst)-x
ans=abs(y-x)
if ans%4==0:
    print("X")
else:
    print('Y')