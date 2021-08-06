import heapq
t = int(input())
for i in range(t):
    k = int(input())
    temp = list(map(int, input().split()))
    files=[]
    result=0
    for i in range(k):
        heapq.heappush(files, temp[i])
    for i in range(k-1):
        a=heapq.heappop(files)
        b=heapq.heappop(files)
        result+=a+b
        heapq.heappush(files, a+b)
    print(result)