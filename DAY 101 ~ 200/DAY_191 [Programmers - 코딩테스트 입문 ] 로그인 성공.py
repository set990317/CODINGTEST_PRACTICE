# [프로그래머스 코딩테스트 입문] - 로그인 성공?
# 블로그 주소 : https://tteum.tistory.com/375

def solution(id_pw, db):
    answer = ''
    dic = {}
    for i in range(len(db)):
        dic[db[i][0]] = db[i][1]
    
    # 입력된 아이디가 dic 안에 키 값으로 있는 경우
    if id_pw[0] in dic :
        # 입력된 비밀번호가 해당 아이디의 비밀번호가 일치할 경우
        if id_pw[1] == dic[id_pw[0]]:
            answer = "login"
        else :
            answer = "wrong pw"
    else :
        answer = "fail"
    return answer