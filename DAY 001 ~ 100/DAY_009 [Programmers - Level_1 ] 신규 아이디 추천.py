# [프로그래머스 Level 1] - 신규 아이디 추천
# 블로그 주소 : https://tteum.tistory.com/140

import re

def solution(new_id):
    answer = ''
    
    new_id = new_id.lower() # 1단계
    new_id = re.sub('[^a-z0-9-_.]', '',new_id) # 2단계
    
    string = list(new_id)   # 3단계
    for i in range(1,len(string)):
        if string[i] == '.':
            if string[i-1] == '.':
                string[i-1] = ''
    new_id = "".join(string)
    
    new_id = new_id.strip('.') # 4단계
    
    if new_id == '': # 5단계
        new_id = 'a'
    
    if len(new_id) >= 16 : # 6단계
        new_id = new_id[:15]    
        if new_id[14] == ".":
            new_id = new_id[:14]
    
    while len(new_id) < 3: # 7단계
        new_id = new_id + new_id[-1]
    
    answer = new_id
    
    return answer