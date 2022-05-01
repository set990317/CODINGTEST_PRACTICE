# [프로그래머스 Level 1] - 이상한 문자 만들기
# 블로그 주소 : https://tteum.tistory.com/173

# 첫 번째 코드 - 실패한 코드
def solution(s):
    answer = ''
    s = s.split(" ") 

    for i in range(len(s)) :
        for j in range(len(s[i])) :
            if j % 2 == 0:
                answer += s[i][j].upper()  
            else : answer += s[i][j]
        if i != (len(s) - 1) : 
              answer += ' '
    return answer

# 두 번째 코드 - 성공한 코드
def solution(s):
    answer = ''
    s = s.lower()
    s = s.split(" ") 
    
    for i in range(len(s)) :
        for j in range(len(s[i])) :
            if j % 2 == 0:
                answer += s[i][j].upper()  
            else : answer += s[i][j]

        if i != (len(s) - 1) : 
              answer += ' '
    return answer