# [프로그래머스 코딩테스트 입문] - 외계행성의 나이
# 블로그 주소 : https://tteum.tistory.com/378

def solution(age):
    alphabet = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
    answer = ''
    age = str(age)
    
    for i in range(len(age)):
        answer += alphabet[age[i]] 
    return answer