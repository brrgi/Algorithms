from collections import deque

OUT = 0
IN =1

def solution(n, start, end, roads, traps):
    queue = deque()
    moveable = {}
    maps = [[-1] * (n+1) for _ in range(n+1)]
    visited = [[False] * (n+1) for _ in range(n+1)]
    traps = set(traps)
    answer = float('inf')
    meet_trap = 0

    for road in roads:
        s, e, w = road
        if s not in moveable.keys():
            moveable[s] = [set(), set()]
        if e not in moveable.keys():
            moveable[e] = [set(), set()]

        moveable[s][OUT].add(e)
        moveable[e][IN].add(s)

        maps[s][e] = w
        maps[e][s] = w
    
    queue.append([start, 0])

    while queue:
        node, time = queue.popleft()

        if node in traps:
            updated_in = set()
            updated_out = set()
            
            for out_elm in moveable[node][OUT]:
                updated_in.add(out_elm)
                
                moveable[out_elm][IN].remove(node)
                moveable[out_elm][OUT].add(node)
            
            for in_elm in moveable[node][IN]:
                updated_out.add(in_elm)
                
                moveable[in_elm][OUT].remove(node)
                moveable[in_elm][IN].add(node)

            moveable[node][OUT] = updated_out
            moveable[node][IN] = updated_in

        
        for next_node in moveable[node][OUT]:
            if visited[node][next_node]: continue
            if next_node == end:
                answer = min(answer, time + maps[node][next_node])
                continue

            queue.append([next_node, time + maps[node][next_node]])
            visited[node][next_node] = True

    return answer

ret = solution(5,	1,	5,	[[1, 3, 4], [1, 2, 3], [3, 4, 1], [2, 4, 10], [4, 5, 1]], [])
# ret = solution(4,	1,	4,	[[1, 3, 4], [1, 2, 3], [3, 4, 1], [2, 4, 10]], [])
# ret = solution(4,	1,	4,	[[1, 2, 4], [1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
# ret = solution(2,	1,	2,	[[1, 2, 3]], [])
print(ret)