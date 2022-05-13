# [프로그래머스 Level 1] - 최소직사각형
# 블로그 주소 : https://tteum.tistory.com/186

def solution(sizes):
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(max(sizes[i][0],sizes[i][1]))
        height.append(min(sizes[i][0],sizes[i][1]))
        
    answer = max(width) * max(height)
    
    return answer