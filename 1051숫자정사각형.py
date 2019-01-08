n,m = map(int,input().split()) #변수 n,m을 한줄에 int형으로 입력받는데 공백으로 구분함.
answer = 0 #answer 변수선언 및 초기화

# grid = [input() for i in range(n)] 이건 아래 세줄을 한줄로 짠 것.
grid = []   #리스트를 만들어서
for i in range(n):   # n을 돌면서 
    grid.append(input())  # 리스트에 입력바든대로 한줄에 덧 붙인다.(세로)    

for size in range(1, min(n,m)+1):
    for y in range(n-size+1):
        for x in range(m-size+1):
            lu = grid[y][x]       #좌표 값(꼭짓점 수)
            ru = grid[y][x+size-1]
            ld = grid[y+size-1][x]
            rd = grid[y+size-1][x+size-1]

            if lu == ru == ld == rd: # 꼭짓점수가 모두 같다.
                answer = size*size

print(answer)            
        
