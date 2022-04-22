# [프로그래머스 Level 1] - 수박수박수박수박수박수?
# 블로그 주소 : https://tteum.tistory.com/164

def solution(n):
    return ("수박"* (n // 2)) + ("수" * (n % 2))