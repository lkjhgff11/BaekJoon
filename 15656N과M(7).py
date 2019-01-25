n,m = map(int,input().split())
nums= list(map(int,input().split()))
nums.sort()

def nums_value(index):
    return nums[index]

def rec(index=0,sec=[]):
    if index==m:
        print(*map(nums_value,sec))
        return

    for i in range(n):
        sec.append(i)
        rec(index+1,sec)
        sec.pop(-1)
rec()        
        
