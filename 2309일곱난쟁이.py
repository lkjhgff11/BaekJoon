nums=[]
for i in range(9):
    n=int(input())
    nums.append(n)

nums.sort()

def comb(startIndex=0,remainder=7,selects=[]):
    if remainder==0:
        if sum(selects)==100:
            print(*selects,sep='\n')
        return

    if startIndex==9:
        return

    for i in range(startIndex,9):
        selects.append(nums[i])
        comb(i+1,remainder-1,selects)
        selects.pop()

comb()
        
