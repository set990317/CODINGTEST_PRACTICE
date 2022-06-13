# [백준] 10809번 - 알파벳 찾기
# 블로그 주소 : https://tteum.tistory.com/220

s =str(input())
alpha = ['a',"b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
result = []
for i in range(26):
    result.append(s.find(alpha[i]))

for i in range(len(result)):
    print(result[i], end = ' ')