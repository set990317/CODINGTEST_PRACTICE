# [프로그래머스 Level 2] - 최댓값과 최솟값
# 블로그 주소 : https://tteum.tistory.com/175

def solution(s):
    answer = ''
    num = s.split()
    num_int = []
    
    for i in range(len(num)):
        num_int.append(int(num[i]))
    answer = str(min(num_int)) + " " + str(max(num_int))  # min, max 넣어서 출력
    
    return answer