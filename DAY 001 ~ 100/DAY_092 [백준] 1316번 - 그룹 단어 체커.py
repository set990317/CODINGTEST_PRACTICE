# [백준] 1316번 - 그룹 단어 체커
# 블로그 주소 : https://tteum.tistory.com/227

# 그룹 단어 체커 함수
def group_word_checker(s):
    already_char = []
    continue_char = s[0];		    		   # 먼저 첫번째 문자 넣어두고 시작
    for i in range(len(s)):
        if s[i] != continue_char:	  		   # 연속 X
            if already_char.count(s[i]) == 0:  # 나온 적 없는 문자라면
                already_char.append(s[i-1])
                continue_char = s[i]
            else:							   # 연속도 아니고, 나온 적도 있다면
                return False
    return True

import sys

n = int(input())		# 여기서 시작						   
answer = 0

for _ in range(n):
    s = str(sys.stdin.readline())
    if group_word_checker(s) == True:
        answer += 1

print(answer)