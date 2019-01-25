n,m = map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
#index는 m까지 늘어나고 n만큼 입력받은 수의 조합. cur은 현재위치.
def rec(index=0,li=[]):
    if index==m:
        print(*li)
        return

    for i in nums:
        if i in li:
            continue

        li.append(i)
        rec(index+1,li)
        li.pop(-1)

rec()        
        

