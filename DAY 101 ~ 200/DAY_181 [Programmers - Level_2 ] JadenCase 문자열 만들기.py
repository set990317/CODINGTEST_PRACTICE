# [프로그래머스 Level 2] - JadenCase 문자열 만들기
# 블로그 주소 : https://tteum.tistory.com/364

def solution(s):
    answer = ''
    s = s.upper()
    s = list(s)
    
    answer += s[0]
    
    for i in range(1,len(s)):
        if s[i-1].isalpha() or s[i-1].isdigit():        
            answer += s[i].lower()
        else :
            answer += s[i]
            
    return answer