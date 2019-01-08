n,m = map(int, input().split())  #한 줄에 n,m을 int형으로 입력받는다
arr = list(range(1,n+1)) #arr은 리스트형으로 범위가 1부터 n까지
arr2 = [] #arr2는 조세퍼스 순열을 담을 배열
index = 0 #index는 0부터
while arr: #arr안을 전부 돌때까지
    index += m-1
    index %= len(arr)
    target = arr.pop(index)
    arr2.append(target)
    # 위에 타겟이랑 그밑에껄 arr.append(arr.pop(index)) 이렇케할수있


print('<',end='') #한줄 안띄우겠따
print(', '.join(map(str,arr2)), end='')
print('>',end='')
# 1 2 3 4 5 6 7

# 사람이 7명까지 있는데, 9번째 사람을 없애라면 2번쨰 사람을 없앤다.
# 사람이 3명까지 있는데, 10번째 사람을 없애라면, 첫번째 사람을 없댄다.
