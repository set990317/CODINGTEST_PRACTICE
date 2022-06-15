# [백준] 1157번 - 단어 공부
# 블로그 주소 : https://tteum.tistory.com/221

s = str(input())
s = s.upper()

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
max = 0
max_alpha = ''
for i in range(26):
    tmp = s.count(alphabet[i])
    if max == tmp :
        if max_alpha != 0:
            max_alpha = '?'
    elif max < tmp :
        max = tmp
        max_alpha = alphabet[i]


print(max_alpha)