# 2007년 1월1일 월요일 2007년 x월y일은 무슨요일일까?
#1,3,5,7,8,10,12월: 31일까지 
#4,6,9,11월: 30일까지
#2월: 28일까지
'''
#외장함수 calendar사용
import calendar
day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
a,b = map(int,input().split())
d=calendar.weekday(2007,a,b)
print(day[d])

'''
#그냥 달력을 구현

a,b = map(int,input().split())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
sum=b
for i in range(a-1):
    sum+=month[i]
d=sum%7
print(day[d])
