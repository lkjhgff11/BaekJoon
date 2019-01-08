t = int(input())
for each_case in range(t):
    a,b = map(int,input().split())
    
    c = pow(a,b,10)
    if not c:
        print(10)
    else:
        print(c)

"""
a ** b
answer = 1
for i in range(b):
    answer *= a

pow(a,b,c)
answer = 1
for i in range(b):
    answer = (answer * a) % c
"""

# iterable
# 반복 가능한 객체

# 시작, 다음

# 1 1 2 3 5 8 13 21 34

