n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
c=0
l=[]
for i in s:
    count=lst.count(i)
    if count==1:
        c=1
        l.append(i)
if c==0:
    print('-1')
else:
    print(max(l))