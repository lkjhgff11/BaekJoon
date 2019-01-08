def rec(n) :
    a = n//10 # 10의 자리
    b = n%10 # 1의 자리
    c = (a+b)%10 # (1의자리 + 10의자리)의 1의자리
    #print(n,a,b,c)
    return (b*10)+c  #새로운 수

n = int(input())
origin_num = n
cnt = 0

while True:
    n = rec(n)
    cnt += 1
    #print(n)
    if n == origin_num:
        break

print(cnt)
