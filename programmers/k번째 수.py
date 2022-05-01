def solution(array, commands):
    answer = []
    
    # i ~ j 까지 자르고 k번째 수를 구하는 배열을 받음
    for i in commands:
        result = array[i[0]-1:i[1]] # array 슬라이싱
        result.sort() # 정렬
        answer.append(result[i[2]-1]) # 인덱스가 0부터 시작되기때문에 -1
    
    return answer
