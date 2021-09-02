from  collections import deque

UP = 'U'
DOWN ='D'
DELETE = 'C'
REVERT = 'Z'
PREV = 0
NEXT = 1

def solution(n, k, cmd):
    linked = {0: [n-1, 1]}
    deleted = []
    
    for val in range(1, n):
        if val == n - 1:
            linked[val] = [val-1, 0]
            continue
        linked[val] = [val - 1, val + 1]
    
    pointer = k
    for elm in cmd:
        splited =  elm.split()

        if splited[0] == UP:

            cnt = 0
            while (cnt < int(splited[1])):
                pointer = linked[pointer][PREV]
                cnt += 1
            continue
        
        if splited[0] == DOWN:

            cnt = 0 
            while (cnt < int(splited[1])):
                pointer = linked[pointer][NEXT]
                cnt += 1
            continue

        if splited[0] == DELETE:
            prev, next = linked[pointer]
            deleted.append([pointer, [prev, next]])

            linked[prev][NEXT] = next
            linked[next][PREV] = prev


            del linked[pointer]

            if next == 0:
                pointer = prev
            else: pointer = next

            continue

        if splited[0] == REVERT:
            node, linked_nodes = deleted.pop()

            linked[node] = linked_nodes
            linked[linked_nodes[PREV]][NEXT] = node
            linked[linked_nodes[NEXT]][PREV] = node

            continue
    
    answer = ''
    for val in range(n):
        if val not in linked.keys():
            answer += 'X'
            continue
        answer += 'O'
    

    return answer
ret = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
print(ret)