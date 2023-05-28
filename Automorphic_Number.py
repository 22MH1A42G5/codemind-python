n=int(input())
no=len(str(n))
sq=n**2
ans=sq%pow(10,no)
if ans==n:
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')