n,m=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()

def convert(index):
    return nums[index]

def rec(index=0,nums2=[],src=0):

    if index==m:
        print(*map(convert,nums2))
        return

    for i in range(src,n):
       
        nums2.append(i)
        rec(index+1,nums2,i)
        nums2.pop(-1)

rec()
