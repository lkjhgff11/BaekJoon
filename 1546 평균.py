#기말고사를 망친 세준이는 점수를 조작해서 집에 가져가기로했는데
#자기 점수중 최댓값 M을 고르고 모든점수를 점수/M*100 으로 위조했다.
#예를들어, 세준이의 최고점이 70점이고 수학점수가 50점이면 세준이의 수학점수는 50/70*100이 되어 71.43점이된다.
#위와 같이 세준이 방식대로 모든 과목 점수가 새로운 점수로 바뀌는데 그 새로운 점수들의 평균을 구해라.
#입력 첫째줄에는 시험본 과목개수 N
#      둘째줄에는 세준이 현재성적
#출력 새로운 평균 출력 10^-2승

n=int(input())
score = list(map(int,input().split()))
m=max(score)

for i in range(n):
             score[i]=score[i]/m*100

avg=sum(score)/len(score)
print("%.2f" %avg)            
             
