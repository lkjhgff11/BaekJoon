n,m=map(int,input().split())

def rec(index=0,nums=[]):

    if index==m:
        print(*nums)
        return

    for i in range(1,n+1):
        nums.append(i)
        rec(index+1,nums)
        nums.pop(-1)

rec()
