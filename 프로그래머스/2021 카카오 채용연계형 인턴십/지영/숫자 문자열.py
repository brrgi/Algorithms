alpha = {
    'zero' : 0,
    'one' : 1, 
    'two': 2,
    'three': 3,
    'four': 4,
    'five' : 5,
    'six': 6,
    'seven': 7 ,
    'eight': 8,
    'nine': 9
}
def solution(s):
    answer = []
    start = 0
    
    while(start < len(s)):
        if s[start].isdigit():
            answer.append(int(s[start]))
            start += 1
            continue
        
        temp = ''
        while(start < len(s) and not s[start].isdigit()):
            temp += s[start]
            start += 1
            if temp in alpha.keys():
                answer.append(alpha[temp])
                break
    
    ret = 0
    for idx, elm in enumerate(answer):
        ret += elm * 10**(len(answer) -1 -idx)

    return ret

print(solution(input()))