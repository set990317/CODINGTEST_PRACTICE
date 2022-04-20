# [프로그래머스 Level 1] - 문자열 내 마음대로 정렬하기
# 블로그 주소 : https://tteum.tistory.com/162

def solution(strings, n):
    strings.sort()
    strings = sorted(strings, key = lambda x:x[n])
    return strings