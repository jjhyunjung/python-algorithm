def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        print(s[len(s) // 2-1])
        answer = s[(len(s) // 2-1) : (len(s) // 2+1)]
    else:
        answer = s[len(s) // 2]
        
    return answer
