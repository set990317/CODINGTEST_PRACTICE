# [프로그래머스 Level 2] - 영어 끝말잇기
# 블로그 주소 : https://tteum.tistory.com/368

def solution(s):
    answer = 0
    dic = {']':'[','}':'{',')':'('}
    
    for _ in range(len(s)):
        stack = []
        flag = 0
        s = s[1:len(s)] + s[0]
        
        for i in range(len(s)):
            if s[i] == '[' or s[i] == '(' or s[i] == '{':
                stack.append(s[i])
            else :
                if len(stack) != 0 :
                    if stack[-1] == dic[s[i]]:
                        stack.pop()
                    else :
                        flag = 1
                        break
                else :
                    flag = 1
                    break

        if flag == 0 and len(stack) == 0:
            answer += 1

    return answer