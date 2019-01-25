n,m = map(int,input().split())
nums= list(map(int,input().split()))
nums.sort()

def convert(index):
    return nums[index]

def rec(index=0,sec=[],cur=0):
    if index==m:
        print(*map(convert,sec))
        return

    for i in range(cur,n):
        if i in sec:
            continue
        sec.append(i)
        rec(index+1,sec,i)
        sec.pop(-1)

rec()
        
