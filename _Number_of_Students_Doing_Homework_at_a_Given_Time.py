n1=int(input())
lst1=list(map(int,input().split()))
n2=int(input())
lst2=list(map(int,input().split()))
q=int(input())
c=0
j=0
for i in lst1:
    if lst2[j]>=q and i<=q:
        c+=1
    j+=1
print(c)