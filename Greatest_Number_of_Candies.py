n=int(input())
lst=list(map(int,input().split()))
lim=int(input())
maxi=max(lst)
for i in lst:
    if i+lim>=maxi:
        print(True,end=' ')
    else:
        print(False,end=' ')