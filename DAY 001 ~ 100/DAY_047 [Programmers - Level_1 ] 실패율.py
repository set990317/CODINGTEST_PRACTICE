# [프로그래머스 Level 1] - 실패율
# 블로그 주소 : https://tteum.tistory.com/180

def solution(N, stages):
    answer = []
    
    clear_user = len(stages)
    fail_dict = {}
    
    for num in range(1,N+1):        # 실패율 계산
        stage_count = stages.count(num) 
        fail = 0
        
        if stage_count != 0:
            fail = stage_count/clear_user    
        fail_dict[num] = fail
        
        clear_user -= stage_count
        
    answer = sorted(fail_dict, key=lambda x: fail_dict[x], reverse=True)
    
    return answer