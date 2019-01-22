n,m=map(int,input().split())

def rec(index=0,nums=[],src=1):
    if index==m:
        print(*nums)
        
    for i in range(src,n+1):
        if i in nums:
            continue
        
        nums.append(i)
        rec(index+1,nums,i+1)
        nums.pop(-1)

rec()
    
