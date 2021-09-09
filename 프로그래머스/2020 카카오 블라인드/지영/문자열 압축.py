def solution(string):
    answer = len(string)
    
    for cp in range(1, len(string)):

        splited = [string[idx : idx+cp] for idx in range(0, len(string), cp)]
        stack = [[splited[0], 1]]


        for elm in range(1, len(splited)):

            if stack[-1][0] == splited[elm]:
                stack[-1][1] += 1
                continue

            stack.append([splited[elm], 1])

        full_Str = ''
        for elm in stack:
            if elm[1] > 1:
                full_Str += str(elm[1]) + elm[0]
                continue
            full_Str += elm[0]
            
        answer = min(answer, len(full_Str))
        

    return answer

print(solution("aabbaccc"))