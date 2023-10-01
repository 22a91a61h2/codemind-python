n=int(input())
m=0
for i in range(2,n):
    if(n%i==0):
        print(i,end=" ")
        m=m+1;
if not m:
    print("-1")