import sys

from collections import deque
input = sys.stdin.readline

N = int(input())
vertexs = deque()

for _ in range(N):
    vertexs.append(list(map(int, input().split())))

# 처음 시작은 y값이 음수에서 시작해야 함.
while vertexs[0][1] > 0:
    vertexs.rotate(-1)

range_list = []
stack = []

cnt = 0
peek = 0
"""
"""
while cnt < N:
    cur = vertexs[0]
    next = vertexs[1]

    # 봉우리의 시작, y > 0
    if cur[1] < 0 and next[1] > 0:
        range_list.append([peek, next[0]])
    
    # 봉우리의 끝, y < 0
    if cur[1] > 0 and next[1] < 0:
        range_list.append([peek, next[0]])
        peek += 1
    
    cnt += 1
    vertexs.rotate(-1)

range_list.sort(key=lambda x: x[1])

# print(range_list)
parents = 0
leaf = 0
has_child = set()
# stack이 빈상태로 특정 값이 들어가는 경우, 부모 봉우리
# stack에 바로 직전에 담긴 봉우리가 현재 봉우리가 같은 봉우리인 경우, 자식이 없는 봉우리
for elm in range_list:
    if not stack: 
        stack.append(elm)
        parents += 1
        continue
    
    if stack[-1][0] == elm[0]: 
        if stack[-1][0] not in has_child:
            leaf += 1
        stack.pop()
        continue

    has_child.add(stack[-1][0])
    stack.append(elm)

print(f"{parents} {leaf}")

