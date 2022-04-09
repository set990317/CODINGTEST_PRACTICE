# [프로그래머스 Level 1] - 3진법 뒤집기
# 블로그 주소 : https://tteum.tistory.com/151

def solution(n):
    reverse_word = ''
    num = 0
    
    while n > 0:
        n, mod = divmod(n, 3)
        reverse_word += str(mod)
    
    return int(reverse_word,3)