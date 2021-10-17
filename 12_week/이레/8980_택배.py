
n,c=map(int, input().split())   #마을 수 n, 트럭의 용량 c
m=int(input())
box = [0] * (n + 1)
boxes=[]
result=0
for i in range(m):
    start, end, cost=map(int, input().split())
    boxes.append([start,end,cost])

boxes.sort(key=lambda x:x[1])   #end를 기준으로 정렬


for s, e, co in boxes:
    print(s,e,co, end = " ")
    max_val = co

    for i in range(s, e):       #start부터 end까지 제일 작은거
        max_val = min(max_val, c - box[i])  #적재 가능한 갯수 - 현재까지 박스의 갯수

    for i in range(s, e):       #트럭에 누적 적재 합을 더해준다.
        box[i] += max_val
    result += max_val
    print(max_val, box, result)

print(result)