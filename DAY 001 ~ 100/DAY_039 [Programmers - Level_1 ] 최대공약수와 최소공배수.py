# [프로그래머스 Level 1] - 최대공약수와 최소공배수
# 블로그 주소 : https://tteum.tistory.com/171

def solution(n, m):
    answer = []
    tmp = 0
    max = 1
    if m < n :
        tmp = n
        n = m
        m = tmp
        
    for i in range(1,n+1):
        if m % i == 0:
            if n % i == 0:  
                max = i
    min = m * n / max
    
    answer.append(max)
    answer.append(min)
    
    return answer