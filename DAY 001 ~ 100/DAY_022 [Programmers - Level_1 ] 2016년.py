# [프로그래머스 Level 1] - 2016년
# 블로그 주소 : https://tteum.tistory.com/154

def solution(a, b):
    mon = [3,1,3,2,3,2,3,3,2,3,2,3]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    for i in range(0,a-1):
        b += mon[i]
    
    b = b % 7 - 1 # index가 0부터 시작하는 걸 고려해서 -1을 해줌.
    
    return day[b]