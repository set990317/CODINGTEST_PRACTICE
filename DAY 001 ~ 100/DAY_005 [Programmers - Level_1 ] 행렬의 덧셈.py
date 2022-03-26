# [프로그래머스 Level 1] - 행렬의 덧셈
# 블로그 주소 : https://tteum.tistory.com/135

def solution(arr1, arr2):
    answer = arr1
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer