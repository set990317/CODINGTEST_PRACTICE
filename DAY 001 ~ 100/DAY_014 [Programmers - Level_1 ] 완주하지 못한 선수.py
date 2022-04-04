# [프로그래머스 Level 1] - 완주하지 못한 선수
# 블로그 주소 : https://tteum.tistory.com/145

def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(0,len(completion)):
        if participant[i] != completion[i] :
                answer = participant[i]
                return answer
                
    answer = participant[-1]
    return answer