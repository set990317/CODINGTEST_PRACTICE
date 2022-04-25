# [프로그래머스 Level 1] - 시저 암호 
# 블로그 주소 : https://tteum.tistory.com/167

def solution(s, n): 
    s = list(s) 
    for i in range(len(s)): 
        if s[i].isupper(): 
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) 
            
        elif s[i].islower(): 
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) 
    
    return "".join(s)