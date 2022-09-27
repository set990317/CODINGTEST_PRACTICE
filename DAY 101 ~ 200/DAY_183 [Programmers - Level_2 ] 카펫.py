# [프로그래머스 Level 2] - 카펫
# 블로그 주소 : https://tteum.tistory.com/366

def solution(brown, yellow):
    
    answer = []

    total = brown + yellow

    for num in range(3,total//2):
        if total % num == 0:
            a = total // num
            b = num
            if (a-2) * (b-2) == yellow :
                answer.append(a)
                answer.append(b)
                break
    answer.sort(reverse=True)
    
    return answer