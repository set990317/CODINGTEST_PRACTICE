# [프로그래머스 Level 2] - 행렬의 곱셈
# 블로그 주소 : https://tteum.tistory.com/371

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    
    # 행렬의 곱셈 식 그대로 코드 작성
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer