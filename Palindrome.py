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
print(palindrome(n))