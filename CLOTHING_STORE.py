su=0
n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
for i in s:
    count=lst.count(i)
    su=su+(int(count/2))
print(su)