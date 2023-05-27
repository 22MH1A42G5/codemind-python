def feb(n):
    a=0
    b=1
    while(a!=n):
        c=a+b
        a=b
        b=c
        if a>n:
            return False
            break
    return True
c=1
cn=0
n=int(input())
i=n
while(n):
    c=c+1
    i=i+1
    if feb(i):
        ans=i
        break
for j in range (n,0,-1):
    cn=cn+1
    if feb(j):
        ans1=j
        break
#print(c,cn)
#print(ans,ans1)
if(c>cn):
    print(ans1)
elif(c<cn):
    print(ans)
else:
    print(ans1,ans)