import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
ins=(s*(s-a)*(s-b)*(s-c))
ans=math.sqrt(ins)
print(format(ans,".2f"))