# [프로그래머스 Level 1] - 숫자 문자열과 영단어
# 블로그 주소 : https://tteum.tistory.com/141

def solution(s):
    answer = 0
    s = s.replace('zero', '0')
    s = s.replace('one','1')
    s = s.replace('two', '2')
    s = s.replace('three','3')
    s = s.replace('four', '4')    
    s = s.replace('five','5')
    s = s.replace('six', '6')    
    s = s.replace('seven','7')
    s = s.replace('eight', '8')    
    s = s.replace('nine','9')
    
    answer = int(s)

    return answer