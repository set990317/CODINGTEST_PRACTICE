# [프로그래머스 Level 1] - 가운데 글자 가져오기
# 블로그 주소 : https://tteum.tistory.com/157

def solution(s):
    answer= ''
    num=0
    if len(s) % 2 == 0:
        num = len(s) // 2 - 1
        return s[num:num+2]
    else : 
        num = len(s) // 2
        
        return s[num]
