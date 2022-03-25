# [프로그래머스 Level 1] - 핸드폰 번호 가리기
# 블로그 주소 : https://tteum.tistory.com/132

def solution(phone_number):
    answer = ''
    len_pn = len(phone_number)
    
    for _ in range(len_pn - 4):
            answer += "*"
    
    for i in range(len_pn - 4, len_pn):
        answer += phone_number[i]
    return answer