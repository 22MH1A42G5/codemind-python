t=int(input())
for i in range (1,t+1):
    n=int(input())
    sn=str(n)
    r=sn[::-1]
    if(int(r)==n):
        print(True)
    else:
        print(False)