n=int(input())
su=0
suo=0
lst=list(map(int,input().split()))
for i in range(0,n):
    if i%2==0:
        su=su+lst[i]
    else:
        suo=suo+lst[i]
if su-suo==0:
    print('YES')
else:
    print('NO')