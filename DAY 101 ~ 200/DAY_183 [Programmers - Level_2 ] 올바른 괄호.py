# [프로그래머스 Level 2] - 올바른 괄호
# 블로그 주소 : https://tteum.tistory.com/366

def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append("(")
        else:
            if len(stack) != 0:
                if stack[-1] == "(":
                    stack.pop()
                else :
                    stack.append(")")
            else :
                stack.append(")")                
    
    if len(stack) != 0 :
        answer = False
    
    return answer