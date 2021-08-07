import sys
input = sys.stdin.readline
import heapq
N = int(input())

def optimize_file_combine(que):
    accumulated_costs = 0
    while len(que) > 1:
        cost = heapq.heappop(que) + heapq.heappop(que)
        accumulated_costs += cost
        heapq.heappush(que, cost)
    print(accumulated_costs)

for _ in  range(N):
    heap = []
    chapter = int(input())
    list(map(lambda elm: heapq.heappush(heap, int(elm)) , input().split()))
    optimize_file_combine(heap)
