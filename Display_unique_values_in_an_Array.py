n=int(input())
lst=list(map(int,input().split()))
c=0
s=set(lst)
for i in s:
    count=lst.count(i)
    if count==1:
        c=1
        print(i,end=' ')
if c==0:
    print('-1')