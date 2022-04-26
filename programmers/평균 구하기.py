def solution(arr):
    answer = 0
    
    # arr에 있는 값을 다 빼서 answer에 더해줌
    for i in range(len(arr)):
        answer += arr[i]
    answer = answer / len(arr)
    return answer
