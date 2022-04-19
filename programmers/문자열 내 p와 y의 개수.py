def solution(s):
    answer = True
    pcnt = 0
    ycnt = 0
    
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            pcnt += 1
        if s[i] == 'y' or s[i] == 'Y':
            ycnt += 1
    
    if pcnt == ycnt:
        answer = True;
    
    else:
        answer = False;

    return answer;
