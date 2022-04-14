# [프로그래머스 Level 1] - [1차] 비밀지도
# 블로그 주소 : https://tteum.tistory.com/156

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        arr1[i] = "{:b}".format(arr1[i]).zfill(n)  # 2진수 변환 및 앞에 0 채우기
        arr2[i] = "{:b}".format(arr2[i]).zfill(n)
        str = ''
        for j in range(n):
            if arr1[i][j] == arr2[i][j] == '0':
                str += " "
            else:
                str += "#"
        answer.append(str)
    
    return answer