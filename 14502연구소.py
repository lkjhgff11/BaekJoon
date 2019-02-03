from pprint import pprint
import math
dx=[1,0,0,-1]
dy=[0,1,-1,0]  # 인접한 네 방향

n,m = map(int,input().split())
nums=[list(map(int,input().split())) for _ in range(n)]
visited=[[False for x in range(m)] for y in range(n)]

maxArea=0
# 벽 3개를 놓는 모든 경우.  
def wall(index,y,x):
    global maxArea
    nums[y][x]=3
  
    if index==3:
        nums2=[line[:] for line in nums]
        for cur_y in range(n):
            for cur_x in range(m):
                if nums[cur_y][cur_x]==2:
                    virus(cur_y,cur_x,nums2)
        safe=safeArea(nums2)
        maxArea=max(safe,maxArea)
                   
    else:
        for cur_y in range(n):
            for cur_x in range(m):
                if nums[cur_y][cur_x]==0:
                    wall(index+1,cur_y,cur_x)
    nums[y][x]=0      # 세운벽 다시 돌리기.          
           
# dfs로 바이러스 확산
def virus(y,x,nums2):
    nums2[y][x]=2
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if ny<0 or nx<0 or ny>=n or nx>=m:
            continue

        if nums2[ny][nx]==0:
            virus(ny,nx,nums2)


# 안전구역 크기 구하기
def safeArea(nums2):
    safe=0
    for y in range(n):
        for x in range(m):
            if nums2[y][x]==0 :
                safe+=1
       
    return safe

for y in range(n):
    for x in range(m):
        if nums[y][x]==0:
            wall(1,y,x)
print(maxArea)
            
