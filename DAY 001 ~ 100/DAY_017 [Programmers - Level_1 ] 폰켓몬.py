# [프로그래머스 Level 1] - 폰켓몬
# 블로그 주소 :https://tteum.tistory.com/149

def solution(nums):
    answer = 0;
    original_nums_len = len(nums) // 2
    nums = set(nums)
    
    if original_nums_len < len(nums) :
        answer = original_nums_len
    else : answer = len(nums)
    
    return answer