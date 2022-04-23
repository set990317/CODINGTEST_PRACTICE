# [프로그래머스 Level 1] - 문자열 내림차순으로 배치하기
# 블로그 주소 : https://tteum.tistory.com/165

def solution(s):
    answer = ''
    lower = []
    upper = []
    
    for char in s :
        if ord(char) <= 96 :
            upper.append(char)
        else : lower.append(char)
    
    upper.sort(reverse = True)
    lower.sort(reverse = True)
    
    result = "".join(lower + upper)
    
    return result