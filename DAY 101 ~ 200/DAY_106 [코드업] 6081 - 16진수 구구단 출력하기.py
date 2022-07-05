# [코드업] 6081 - 16진수 구구단 출력하기
# 블로그 주소 : https://tteum.tistory.com/243

s = int(input(),16)

for i in range(1,16):
    print('{0}*{1}={2}'.format(format(s,'x').upper(),format(i,'x').upper(),format((s*i), 'x').upper()))