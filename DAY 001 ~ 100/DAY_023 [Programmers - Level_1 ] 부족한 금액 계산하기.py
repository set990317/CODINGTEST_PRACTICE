# [프로그래머스 Level 1] - 부족한 금액 계산하기
# 블로그 주소 : https://tteum.tistory.com/155

def solution(price, money, count):
    answer = -1
    total = 0;
    
    for num in range(1,count+1):
        total += price * num
    
    if total - money < 0:
        answer = 0
    else : answer = money - total
    
    return abs(answer)