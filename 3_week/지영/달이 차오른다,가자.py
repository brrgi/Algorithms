N, M = map(int, input().split())
maze = []
queue = []
arrived = 0
ret = 10 ** 10
visited = [[[False for  _ in range(65)] for _ in range(M)] for _ in range(N)]
key_order = {'a': 0, 'b': 1, 'c': 2,'d':3, 'e':4,'f':5}
# 입력 받으면서 현 위치 queue에 세팅
for x in range(N):
    maze.append([])
    for y, input_elm in enumerate(input()):
        maze[x].append(input_elm)
        if input_elm == '0':
            queue.append([x,y,0, 0b000000])
            visited[x][y][0] =True

while queue:
    x, y, dist, key = queue.pop(0)
    cur_val = maze[x][y]
    
    if cur_val == '1':
        ret =  min(ret, dist)
        arrived += 1
        continue

    for elm in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        temp_key = key
        x_pos = x + elm[0]
        y_pos = y + elm[1]

        if 0 > x_pos or 0 > y_pos or N <= x_pos or M <= y_pos: continue
        if maze[x_pos][y_pos] == '#': continue
        if visited[x_pos][y_pos][temp_key]: continue
        # 시간을 줄이기 위해 가치지기 과정을 추가한다.
        # 열쇠가 없는 경우도 사전에 가지치기 
        if maze[x_pos][y_pos].isupper() and maze[x_pos][y_pos].lower() in key_order.keys():
            if not temp_key & (1 << key_order[maze[x_pos][y_pos].lower()] - key_order['a']): continue
        # 이미 같은 열쇠를 가지고 있는 경우도 사전에 가지치기
        if maze[x_pos][y_pos].islower() and maze[x_pos][y_pos] in key_order.keys():
            # 이미 같은 열쇠를 가지고 있는 경우
            if temp_key & (1 << key_order[maze[x_pos][y_pos]] - key_order['a']): continue
            temp_key = temp_key | (1 << key_order[maze[x_pos][y_pos]] - key_order['a'])
            if visited[x_pos][y_pos][temp_key]: continue

        queue.append([x_pos, y_pos, dist+1, temp_key])
        visited[x_pos][y_pos][temp_key] = True

print(ret) if arrived != 0 else print(-1)

"""
    열쇠를 찾은 경우, visited를 초기화 했다는 것
"""