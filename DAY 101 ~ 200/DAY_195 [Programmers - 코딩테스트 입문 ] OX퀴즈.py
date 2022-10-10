# [프로그래머스 코딩테스트 입문] - OX퀴즈
# 블로그 주소 : https://tteum.tistory.com/380

def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        tmp = quiz[i].split(" ")
        if tmp[1] == '+':
            if int(tmp[0]) + int(tmp[2]) == int(tmp[4]):
                answer.append("O")
                continue
            answer.append("X")
        else :
            if int(tmp[0]) - int(tmp[2]) == int(tmp[4]):
                answer.append("O")
                continue
            answer.append("X")                
    return answer