n1=int(input())
lst1=list(map(int,input().split()))
j=0
n2=int(input())
ans=[]
lst2=list(map(int,input().split()))
for i in lst1:
    ans.insert(lst2[j],i)
    j+=1
for i in ans:
    print(i,end=' ')