from pprint import pprint
n=5#int(input())

li=[['*'for i in range(n*2)]for i in range(1,n*2)]
for y in range(n):
    start = y + 1
    end = n * 2 - (y + 1)
    for x in range(start, end):
        li[y][x] = ' '

for y in range(n-1):
    start = n - 1 - y
    end = n + 1 + y
    for x in range(start, end):
        li[y+n][x] = ' '

for l in li:
    print(''.join(l))
