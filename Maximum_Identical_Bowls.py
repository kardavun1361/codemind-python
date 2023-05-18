def identical(a,b,c):
    for i in range(c,0,-1):
        if(b%i==0):
            return i
    else:
        return 0

c=int(input())
a=list(map(int,input().split()))
b=sum(a)
print(identical(a,b,c))