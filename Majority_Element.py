n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
maxi=0
for i in s:
    if lst.count(i)>maxi:
        ans=i
        maxi=lst.count(i)
print(ans)