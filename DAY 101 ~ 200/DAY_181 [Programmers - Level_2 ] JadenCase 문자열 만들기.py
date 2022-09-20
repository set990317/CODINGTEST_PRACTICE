# [프로그래머스 Level 2] - JadenCase 문자열 만들기
# 블로그 주소 : https://tteum.tistory.com/364

def solution(s):
    answer = ''
    s = s.lower()

    s_list = []

    s_list = s.split(" ")
    for i in range(len(s_list)):
        if len(s_list[i]) != 0 :
            if s_list[i][0].isalpha() == True :
                s_list[i] = s_list[i].capitalize()
    
    print(s_list)


    
    return answer