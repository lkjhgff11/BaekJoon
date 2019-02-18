# 컵 위치를 바꾼횟수 M, X와 Y는 컵의 위치를 바꾼방법.
# 4
# 3 1
# 2 3
# 3 1
# 3 2
# 컵 3개 제일처음 공은 1번컵에 있음. 공이 있을때는 1 없을때는 0

# 배열로 풀기

ball=['b',1,0,0]
for i in range(int(input())):
    x,y=map(int,input().split())
    ball[x],ball[y]=ball[y],ball[x]

print(ball.index(1))    


# 배열을 쓰지않고, 문자열포맷, exec 이용해서 풀기
'''
one=1
two=0
three=0

for _ in range(int(input())):
    x,y=map(int,input().split())  # 3 1 , 2 3 ,3 1, 3 2
    x=['one','two','three'][x-1]
    y=['one','two','three'][y-1]
    query = '%s,%s = %s,%s'%(x,y,y,x)
    exec(query)

if one:
    print(1)
if two:
    print(2)
if three:
    print(3)
    
'''

    
    
