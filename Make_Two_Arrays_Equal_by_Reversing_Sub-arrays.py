n1=int(input())
lst1=list(map(int,input().split()))
n2=int(input())
lst2=list(map(int,input().split()))
lst1.sort()
lst2.sort()
if lst1==lst2:
    print(True)
else:
    print(False)