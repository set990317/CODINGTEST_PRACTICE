# [프로그래머스 Level 2] - 기능개발
# 블로그 주소 : https://tteum.tistory.com/365

def solution(progresses, speeds):
    answer = []
    day = []
    count = 1
    
    

    # 1. for문을 이용해 각각 언제 배포 가능해지는 지 append.
    for i in range(len(progresses)):
        tmp = 100 - progresses[i]
        
        if tmp % speeds[i] == 0:
            day.append(tmp//speeds[i])
        else :
            day.append(tmp//speeds[i]+1)
    
    a = day[0]

    # 2. day 리스트 앞에 숫자보다 뒤에 숫자가 더 작다면 +, 아니라면 append.
    for i in range(1,len(day)):
        if a >= day[i]:
            count += 1
        else:
            a = day[i]
            answer.append(count)
            count = 1
            
    answer.append(count)
    
    return answer