import heapq
n,c=map(int, input().split())   #마을 수 n, 트럭의 용량 c
m=int(input())
for i in range(m):
    start, end, cost=map(int, input().split())
