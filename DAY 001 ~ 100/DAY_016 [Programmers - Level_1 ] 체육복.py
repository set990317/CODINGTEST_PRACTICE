# [프로그래머스 Level 1] - 체육복
# 블로그 주소 : https://tteum.tistory.com/148


def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    
    for num in lost[:] :
        if num in reserve[:]:
            reserve.remove(num)
            lost.remove(num) 
    
    for num in lost[:] :
        if num-1 in reserve[:] :
            reserve.remove(num-1)
            lost.remove(num)
        elif num+1 in reserve[:] :
            reserve.remove(num+1)
            lost.remove(num)
            
    answer = n - len(lost)
    return answer