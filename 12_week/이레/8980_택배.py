import sys
input=sys.stdin.readline
n,c=map(int, input().split())   #마을 수 n, 트럭의 용량 c
m=int(input())
box = [0] * (n + 1)
boxes=[]
result=0
for i in range(m):
    start, end, cost=map(int, input().split())
    boxes.append([start,end,cost])
# print(boxes)
boxes.sort(key=lambda x:x[1])
# print(boxes)

for s, d, co in boxes:
    max_val = co
    for i in range(s, d):
        max_val = min(max_val, c - box[i])
    for i in range(s, d):
        box[i] += max_val
    result += max_val
print(result)