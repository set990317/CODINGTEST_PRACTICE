# [프로그래머스 Level 2] - 최솟값 만들기
# 블로그 주소 : https://tteum.tistory.com/176

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        answer += A[i] * B[i]
            
    return answer