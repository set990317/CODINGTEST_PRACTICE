# [백준] 10988번 - 팰린드롬인지 확인하기
# 블로그 주소 : https://tteum.tistory.com/305

word = str(input())
result = 1

if len(word) % 2 != 0: # 단어가 홀수인 경우
    tmp = len(word) // 2
    word_1 = word[0:tmp]
    word_2 = word[tmp+1:len(word)]
else :                 # 단어가 짝수인 경우
    tmp = len(word) // 2 - 1
    word_1 = word[0:tmp+1]
    word_2 = word[tmp+1:len(word)]

word_2 = word_2[::-1]

for i in range(len(word_1)):
    if word_1[i] != word_2[i]:
        result = 0
        break

print(result)