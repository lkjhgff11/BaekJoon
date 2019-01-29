n=int(input())
nums=list(map(int,input().split()))

def Prime(n):
    if n<2:
        return 0
    for i in range(2,n-1):
        if n%i==0:
            return 0
    return 1

cnt=0
for i in nums:  
    Prime(i)
    cnt+=Prime(i)
print(cnt)
