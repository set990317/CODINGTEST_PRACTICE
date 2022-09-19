# [프로그래머스 Level 2] - 숫자의 표현
# 블로그 주소 : https://tteum.tistory.com/362

def solution(n):
    answer = 0
    for i in range(1,n+1):
        tmp = 0
        
        for j in range(i,n+1):
            tmp += j            
            
            if tmp > n :
                break
            elif tmp == n :
                answer += 1
                break
    
    return answer