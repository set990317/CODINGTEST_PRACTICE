# [프로그래머스 Level 1] - 두 개 뽑아서 더하기
# 블로그 주소 : https://tteum.tistory.com/153

# 첫 번째 코드
def solution(numbers):
    answer = []
    
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    answer = list(set(answer))
    answer.sort()

    return answer

# 두 번째 코드    
def solution(numbers):
    answer = []
    
    
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if i == j :
                answer.append(numbers[i]+numbers[j])
                continue;
            answer.append(numbers[i]+numbers[j])
    
    answer = list(set(answer))
    answer.sort()

    return answer