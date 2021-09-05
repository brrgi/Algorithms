import heapq
import sys

n = int(input())
results = [0 for i in range(100000)]
start = sys.maxsize
end = -1
queue = []

chair = [i + 1 for i in range(100000)]
heapq.heapify(chair)

humans = []
for i in range(n):
    t = list(map(int, input().split()))
    start = min(start, t[0])
    end = max(end, t[1])
    humans.append(t)
humans.sort(key=lambda x: x[0])

ind = 0
for i in range(start, end + 1):
    if ind < n and i == humans[ind][0]:
        temp = heapq.heappop(chair)
        results[temp] += 1
        heapq.heappush(queue, (humans[ind][1], temp))  # 우선순위, 값
        ind += 1
        continue

    if i == queue[0][0]:
        temp = heapq.heappop(queue)
        heapq.heappush(chair, temp[1])
        continue

print(len(results) - results.count(0))
for i in range(len(results) - results.count(0)):
    print(results[i + 1], end=" ")
