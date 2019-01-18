from pprint import pprint 
import sys
sys.setrecursionlimit(100000)
        
dy=[1,0,-1,0]
dx=[0,1,0,-1]
        
def dfs(y,x):
    visited[y][x]=1

    for i in range(4): #배추벌레가 4방향으로 움직이는거
        ny=y+dy[i]
        nx=x+dx[i]

        if ny>=n or nx>=m or ny<0 or nx<0:
            continue

        elif grid[ny][nx]==1 and visited[ny][nx]==0:
            grid[ny][nx]=0
            dfs(ny,nx)

  
t= int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    grid=[[0 for x in range(m)]for y in range(n)]
    visited=[[0 for x in range(m)]for y in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        grid[y][x]=1

    cnt=0      
    for y in range(n):
        for x in range(m):
            if grid[y][x]==1 and visited[y][x]==0:
              #  print(y,x)
                dfs(y,x)
                
                '''
                print('-------')
                print(y,x)
                print('visted')
                pprint(visited)
                print('grid')
                pprint(grid)
                '''
                cnt+=1
          
    print(cnt)

    


