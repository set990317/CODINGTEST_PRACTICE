# [프로그래머스 Level 2] - 전화번호 목록
# 블로그 주소 : https://tteum.tistory.com/177

def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
    return answer