# [프로그래머스 Level 2] - 피보나치 수
# 블로그 주소 : https://tteum.tistory.com/363

def solution(n):
    answer = 0
    fibo = [1,1]
    
    for i in range(n):
        fibo.append(fibo[i]+fibo[i+1])
    
    answer = fibo[n-1] % 1234567
    return answer