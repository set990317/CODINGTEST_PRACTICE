# [프로그래머스 코딩테스트 입문] - 모스부호 (1)
# 블로그 주소 : https://tteum.tistory.com/373

def solution(letter):
    # 모스부호 (딕셔너리)
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'}

	answer = ''
    
    letter = letter.split(" ")
    
    # 딕셔너리를 이용해 answer에 글자 하나씩 넣기
    for i in range(len(letter)):
        answer += morse[letter[i]]
        
    return answer