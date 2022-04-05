# [프로그래머스 Level 1] - K번째수
# 블로그 주소 :https://tteum.tistory.com/146

def solution(array, commands):
    answer = []
    slice_array = []
    for i in range(0, len(commands)):
        a = commands[i][0] - 1
        b = commands[i][1]
        c = commands[i][2] - 1

        slice_array = array[a:b]
        slice_array.sort()
        answer.append(slice_array[c])
        
    return answer