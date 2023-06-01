n=int(input())
lst=list(map(int,input().split()))
lst.sort()
i=1
while(True):
    if i in lst:
        i+=1
    else:
        print(i)
        break