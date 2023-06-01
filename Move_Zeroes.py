n=int(input())
lst=list(map(int,input().split()))
cz=lst.count(0)
for i in lst:
    if i!=0:
        print(i,end=' ')
for i in range(1,cz+1):
    print('0',end=' ')