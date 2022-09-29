# [프로그래머스 코딩테스트 입문] - 배열 두 배 만들기
# 블로그 주소 : https://tteum.tistory.com/372

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(numbers[i]*2)
    return answer