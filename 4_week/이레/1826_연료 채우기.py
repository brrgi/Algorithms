import heapq

n = int(input())
stations = []
for i in range(n):
    a, b = map(int, input().split())
    stations.append((a, b))
l, p = map(int, input().split())
stations = sorted(stations, key=lambda x: x[0])     #처음에 정렬하기

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

if p < l:               #마을에 도착하지 못할 경우
    result = -1
print(result)