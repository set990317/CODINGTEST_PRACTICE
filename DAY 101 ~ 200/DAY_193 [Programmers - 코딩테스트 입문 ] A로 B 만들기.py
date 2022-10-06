# [프로그래머스 코딩테스트 입문] - A로 B 만들기
# 블로그 주소 : https://tteum.tistory.com/377

def solution(before, after):
    answer = 1
    before = list(before)
    after = list(after)
    
    before.sort()
    after.sort()
    
    if after != before :
        answer = 0
        
    return answer