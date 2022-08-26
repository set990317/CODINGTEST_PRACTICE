# [백준] 1924번 - 2007년
# 블로그 주소 : https://tteum.tistory.com/308

day_of_month = [31,28,31,30,31,30,31,31,30,31,30,31]
month, day = map(int,input().split())
day_of_week = ['SUN','MON','TUE','WED','THU','FRI','SAT']

for i in range(month-1):
    day += day_of_month[i]

day = day % 7

print(day_of_week[day])