# [프로그래머스 Level 1] - 성격 유형 검사하기
# 블로그 주소 : https://tteum.tistory.com/351

def solution(survey, choices):
    answer = ""
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    kakao = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    kind = ['RT','CF','JM','AN']
    
    for i in range(len(choices)):
        tmp = choices[i]
        if tmp < 4 :
            kakao[survey[i][0]] += score[tmp]
        elif 4 < tmp :
            kakao[survey[i][1]] += score[tmp]
    
    for i in range(len(kind)):
        if kakao[kind[i][0]] > kakao[kind[i][1]]:
            answer += kind[i][0]
        elif kakao[kind[i][0]] < kakao[kind[i][1]]:
            answer += kind[i][1]
        else :
            answer += kind[i][0]
            
    return answer