n = int(input())
s=0
m = n*n
while m>0:
    s = s+m%10
    m=m//10
if(n==s):
    print("Neon Number")
else:
    print("Not Neon Number")