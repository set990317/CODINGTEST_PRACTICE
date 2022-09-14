# [프로그래머스 Level 2] - 이진 변환 반복하기
# 블로그 주소 : https://tteum.tistory.com/331

def solution(s):
    answer = []
    change_count = 0
    zero_count = 0

    while(s != '1'):
        zero_count += s.count('0')
        s = format(int(len(s)-s.count('0')),'b')
        change_count += 1

    answer.append(change_count)
    answer.append(zero_count)
    
    return answer