import string
s=input()
alpha={c:-1 for c in string.ascii_lowercase} #a부터z까지 하나하나 받아서 각각 -1로 value들 채워줌
for i in range(len(s)): # 입력받은 문자열 길이만큼 하나하나 도는데
    if alpha[s[i]] == -1: #alpha[s[i]] 입력받은 문자 하나가 -1이라는건 처음에는 -1이니깐 처음등장했다는거고
        alpha[s[i]]=i;  #딕셔너리 alpha의 해당알파벳에 그 알파벳이 처음등장한 위치 저장
                        #Key에 해당하는 알파벳에 Value에 해당하는 처음등장한인덱스위치를 넣음


for key in sorted(alpha.keys()): # key값을abcd~이런식으로 정렬. 왜냐하면 하나하나넣었어도 딕셔너리안에는 순서없이 들어있을확률이높음(딕셔너리 순서없음)) 
    print(alpha[key], end=' ') #print(alpha[key])하면 key에 해당하는 value들이 출력된다.
        




 

