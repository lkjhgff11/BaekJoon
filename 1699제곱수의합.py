n = input()
# 32
# 44 =16 44 = 16
# 76
# 88=64 33=9 11=1= 11=1= 11=1

#제곱을 했을때 그 숫자를 넘어가지않는다면 거기서부터 까내려야 최소에 가깜게 빨리구해진다.
#남은거는 재귀로

# rec는 num을 구성하는 제곱수의 갯수
# ex) 76
# 1 + 12를 구성하는 제곱수의 갯수
def rec(num):
    for i in reversed(range(1,num+1)):
        if i * i == num:
            print(i*i)
            return 1
        if i * i < num:
            print(i*i)
            return 1 + rec(num - i * i)

print(rec(int(n)))
