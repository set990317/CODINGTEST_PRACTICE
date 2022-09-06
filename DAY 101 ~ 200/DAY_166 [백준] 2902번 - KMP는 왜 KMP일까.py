# [백준] 2902번 - KMP는 왜 KMP일까?
# 블로그 주소 : https://tteum.tistory.com/323

text = list(map(str,input().split('-')))
result = ''

for i in range(len(text)):
    result += text[i][0]

print(result)