pos = set({'-', '_', '.'})
def solution(new_id):
    new_id = new_id.lower()
    # 2단계
    answer = ''
    for word in new_id:
        if word.isalnum() or word in pos:
            answer += word
    # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    if answer and answer[0] == '.': answer = answer[1:]
    
    if answer and answer[-1] == '.': answer = answer[:-1]
         
    if len(answer) == 0: answer = 'a'
    
    # 6-1댠계
    if len(answer) > 15: answer = answer[:15]
    
    # 6-2단계
    if answer and answer[-1] == '.': 
        answer = answer[:-1]
        
    # 7단계
    if len(answer) <= 2: 
        while(len(answer) != 3):
            answer+= answer[-1]
    
    return answer

print(solution("+.+"))