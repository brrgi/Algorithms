import heapq
import sys

v,e=map(int, input().split())
k=int(input())  #시작위치
INF=sys.maxsize
distance=[[] for _ in range(v+1)]

for _ in range(e):
    start, end, dist=map(int, input().split())
    distance[start].append([end, dist])

queue=[]
K_distance=[INF for _ in range(v+1)]
K_distance[k]=0
heapq.heappush(queue, [0,k])    #거리랑 정점
while queue:
    mid=heapq.heappop(queue)
    for end in distance[mid[1]]:
        if K_distance[end[0]]>mid[0]+end[1]:
            K_distance[end[0]]=mid[0]+end[1]
            heapq.heappush(queue, [K_distance[end[0]], end[0]])