# [프로그래머스 Level 1] - [1차] 다트 게임
# 블로그 주소 : https://tteum.tistory.com/158

import re

dic = {'S':1,'D':2,'T':3}
dic2 = {'*':2,'#':-1}

def solution(dartResult):
    answer = [] # 합계 낼거임.
    num = 0
    index = -1

    numbers = re.findall("\d+", dartResult) # 숫자 따로 추출
    dartResult = re.sub(r"[^SDT*#]","",dartResult) # 숫자 제거
    
    for char in dartResult:
        if char in dic :
            answer.append(num)
            index += 1
            num = int(numbers[index])
            num = num ** dic[char]
            continue
        if char in dic2 :
            if char == '*':
                if len(answer) != 1: 
                    answer[-1] *= 2
                num *= 2
            else:
                num *= -1

    answer.remove(answer[0])
    answer.append(num)
    return sum(answer)