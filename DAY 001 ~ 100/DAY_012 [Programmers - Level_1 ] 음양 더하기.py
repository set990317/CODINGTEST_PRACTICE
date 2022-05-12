# [프로그래머스 Level 1] - 음양 더하기
# 블로그 주소 : https://tteum.tistory.com/143

def solution(absolutes, signs):
    answer = 0;
    
    for i in range(0,len(absolutes)) :
        if signs[i] == True :
            answer += absolutes[i]
        else : answer -= absolutes[i]

    return answer