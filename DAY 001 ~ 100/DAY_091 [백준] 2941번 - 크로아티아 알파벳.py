# [백준] 2941번 - 크로아티아 알파벳
# 블로그 주소 : https://tteum.tistory.com/226

import sys

s = str(sys.stdin.readline())
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0

# 일치하는 거 추려서 count에 더해주고 원본에서는 없애기
for string in croatia :
    if string in s :
        count += s.count(string)
        s = s.replace(string,' ')

# 남은 거 처리
s = s.replace(' ','') # 그 테트리스마냥 촥촥 되는 거 방지.
s = list(s)
count = count + len(s) - 1  # list로 바꾸는 과정에서 개행문자가 list에 포함되어 -1을 해줌.

print(count)