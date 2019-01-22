# n 과 m이 주어질때 1부터 n까지 자연수 중에서 중복없이 m개를 고른 수열
# 순열을 재귀로 짜기.
#순서 보관하는 리스트 nums=[]
#print(*nums) 배열 하나하나 접근해서 하나하나 출력 

n,m = map(int,input().split())
def rec(index=0,nums = []):
    if index==m:
        print(*nums)
        return
              
    for i in range(1,n+1):
        if i in nums:
            continue
        nums.append(i)
        rec(index+1,nums)
        nums.pop(-1)
        
rec()
