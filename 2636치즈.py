# 공기 0 , 치즈 1
import sys
sys.setrecursionlimit(100000)

n,m = map(int,input().split())
maps=[list(map(int,input().split())) for i in range(n)]
visited=[[ 0 for x in range(m)] for y in range(n)]

dy=[-1,1,0,0]
dx=[0,0,1,-1]

def init_visit():
    for y in range(n):
        for x in range(m):
            visited[y][x]=0

# dfs는 (0,0)부터 시작해서 공기(0)을 퍼트리는식으로 한다. 공기가 퍼져나가면서 방문체크한다.
# 만약 공기가 퍼져나가던중 치즈(1)을 만나면 녹여서 공기(0)로만든다.
def dfs(y,x):
    visited[y][x]=1
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]

        if ny>=n or nx>=m or ny<0 or nx<0:continue  

        #치즈를 발견하고 방문한적이없으면 치즈녹이고 녹인자리 방문했다고 체크
        elif maps[ny][nx]==1 and visited[ny][nx]==0:
            maps[ny][nx]=0
            visited[ny][nx]=1

        elif maps[ny][nx]==0 and visited[ny][nx]==0:
            dfs(ny,nx)
           
time=0
prev_cnt=0
while(1):
    cnt=0
    for y in range(n):
        for x in range(m):
            if maps[y][x]==1:
                cnt+=1
                prev_cnt=cnt   
    if cnt==0:
        print(time)
        print(prev_cnt)
        break
    time+=1
    init_visit()   
    dfs(0,0)

