t = int(input())
for i in range(t):
    r,s = input().split()
    print("".join(m*int(r) for m in s)) # 변수 s로 입력받은 문자열을 문자 하나하나  m에 담아서 r번 반복한거를  공백없이 이어붙인다. 
