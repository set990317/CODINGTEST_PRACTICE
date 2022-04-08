# [프로그래머스 Level 1] - 약수의 개수와 덧셈
# 블로그 주소 : https://tteum.tistory.com/150

def solution(left, right):
    answer = 0
    count = 1          # 약수 1 때문에 count = 1임. 
    
    for num in range(left, right+1):
        for i in range(2,num+1):
            if num % i == 0:
                count += 1
        if count % 2 == 0:
            answer += num
            count = 1        
        else : 
            answer -= num
            count = 1
    return answer