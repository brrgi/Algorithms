import heapq

n = int(input())
stations = []
for i in range(n):
    a, b = map(int, input().split())
    stations.append((a, b))
l, p = map(int, input().split())
stations = sorted(stations, key=lambda x: x[0])

result = 0
ind = 0
heap = []
while p < l:
    temp = ind
    for i in range(ind, n):
        if stations[i][0] <= p:
            heapq.heappush(heap, -stations[i][1])
            temp += 1
    ind = temp
    if heap == []:
        break

    p -= heapq.heappop(heap)
    result += 1

if p < l:
    result = -1
print(result)