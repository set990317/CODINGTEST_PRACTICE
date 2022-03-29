# [프로그래머스 Level 1] - 로또의 최고 순위와 최저 순위
# 블로그 주소 : https://tteum.tistory.com/138

# 첫번째 버전 - 조금 길고 복잡함.

def solution(lottos, win_nums): 
    answer = []
    count = 0;
    zero_count = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            count += 1;
    
    if count == 0 :
        answer.append(6)
        if zero_count == 0:
            answer.insert(0,answer[0]-zero_count) 
        else : answer.insert(0,answer[0]-zero_count+1) 
    elif count == 1 :
        answer.append(6)
        answer.insert(0,answer[0]-zero_count) 
    elif count == 2 :
        answer.append(5)
        answer.insert(0,answer[0]-zero_count) 
    elif count == 3 :
        answer.append(4)
        answer.insert(0,answer[0]-zero_count) 
    elif count == 4 :
        answer.append(3)
        answer.insert(0,answer[0]-zero_count) 
    elif count == 5 :
        answer.append(2)
        answer.insert(0,answer[0]-zero_count) 
    elif count == 6 :
        answer.append(1)
        answer.insert(0,1) 
    
    return answer

# 두번째 버전 - 간결하게 코드를 요약함.

def solution(lottos, win_nums):
    answer = []
    count = 0;
    zero_count = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            count += 1;
    
    if count == 0 :
        answer.append(6)
        if zero_count == 0:
            answer.insert(0,answer[0]-zero_count) 
        else : answer.insert(0,answer[0]-zero_count+1) 
    else : 
        answer.append(7-count)
        answer.insert(0,answer[0]-zero_count)     

    return answer