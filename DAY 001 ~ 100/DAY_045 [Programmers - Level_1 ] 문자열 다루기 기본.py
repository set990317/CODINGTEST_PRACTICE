# [프로그래머스 Level 1] - 문자열 다루기 기본
# 블로그 주소 : https://tteum.tistory.com/178

def solution(s):
    answer = True
    
    if (len(s)==4 or len(s)==6):
        myNum2=True
    else : myNum2=False
        
    if s.isdigit()==True:
        myNum=True
    else:
        myNum=False
    
    answer=myNum and myNum2
    return answer