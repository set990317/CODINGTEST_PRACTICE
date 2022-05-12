# [프로그래머스 Level 1] - 나머지가 1이 되는 수 찾기
# 블로그 주소 : https://tteum.tistory.com/185

def solution(n):
    
    for i in range(1,n):
        if n % i == 1:
            return i