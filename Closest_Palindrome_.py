def palindrome(p):
    t=p
    rev=0
    while (t!=0):
        r=t%10
        rev=rev*10+r
        t=t//10
    if rev==p:
        return True
    else:
        return False
n=int(input())
for i in range(n-1,1,-1):
    
    if palindrome(i):
        a=i
        break
i = n+1
while True:
    if palindrome(i):
        b=i
        break
    i+=1
if n-a == b-n:
    print(a,b)
elif n-a>b-n:
    print(b)
else:
    print(a)