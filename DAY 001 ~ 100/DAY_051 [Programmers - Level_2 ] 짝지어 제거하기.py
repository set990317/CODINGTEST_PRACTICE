# [프로그래머스 Level 2] - 짝지어 제거하기
# 블로그 주소 : https://tteum.tistory.com/184

def solution(s):
    answer = -1
    stack = []
    
    for i in range(len(s)):
        if len(stack) != 0 :
            if stack[-1] == s[i]:
                stack.pop()
            else :
                stack.append(s[i])
        else : stack.append(s[i])
    
    if len(stack) == 0:
        answer = 1
    else : answer = 0
    
    return answer