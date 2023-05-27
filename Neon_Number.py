sm=0
n=int(input())
s=n*n
while s!=0:
    r=s%10
    sm=sm+r
    s=s//10
if(sm==n):
    print('Neon Number')
else:
    print('Not Neon Number')