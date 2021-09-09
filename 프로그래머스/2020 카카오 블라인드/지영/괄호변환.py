"""
    1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    4-3. ')'를 다시 붙입니다. 
    4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    4-5. 생성된 문자열을 반환합니다.

    )(
    입출력 예 #2
    두 문자열 u, v로 분리합니다.
    u = ")("
    v = ""
    u가 "올바른 괄호 문자열"이 아니므로 다음과 같이 새로운 문자열을 만듭니다.
    v에 대해 1단계부터 재귀적으로 수행하면 빈 문자열이 반환됩니다.
    u의 앞뒤 문자를 제거하고, 나머지 문자의 괄호 방향을 뒤집으면 ""이 됩니다.
    따라서 생성되는 문자열은 "(" + "" + ")" + ""이며, 최종적으로 "()"로 변환됩니다.
"""
RIGHT = '('
LEFT = ')'

def dfs(p):
    if p == '': return p
    # u, v로 분리합니다.
    right, left = 0, 0
    u = ''

    for s in p:
        if s == RIGHT: right += 1
        if s == LEFT: left += 1
        
        u += s
        if right == left: break
    
    v = p[right+left:]


    # u가 올바른 문자열 이라면 v에 대해 1단계부터 다시 수행합니다.
    stack = []
    right_string = True
    for s in  reversed(u):
        if s == LEFT:
            stack.append(s)
            continue
        
        if s == RIGHT:
            if len(stack) < 1: 
                right_string = False
                break
            stack.pop()

    if len(stack) > 0: right_string = False

    if right_string: 
        return u + dfs(v)
    
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    if len(u) > 0: updated_u = u[1:]
    if len(u) > 0: updated_u = updated_u[:-1]

    completed = []
    for elm in updated_u:
        if elm == RIGHT: completed.append(LEFT)
        if elm == LEFT: completed.append(RIGHT)



    return '(' + dfs(v) + ')' + ''.join(completed)
    


def solution(p):
    answer = dfs(p)

    return answer


print(solution('()))((()'))