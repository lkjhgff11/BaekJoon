n,m=map(int,input().split())
# count는 m개까지만 출력되도록 갯수 새는거, cur은 현재위치
def rec(count=0,nums=[],cur=1):
    if count==m:
        print(*nums)
        return

    for i in range(cur,n+1): #1다음 1 2 다음 2부터 되도록 처음값을 현재위치로 줌
        nums.append(i)
        rec(count+1,nums,i)
        nums.pop(-1)

rec()
        
        
