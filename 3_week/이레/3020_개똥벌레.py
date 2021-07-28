n, h = map(int, input().split())
top = []
bottom = []
ans = [0 for i in range(h)]

for i in range(n):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
bottom.sort()

for i in range(1, h + 1):
    start = 0
    end = len(top) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if top[mid] >= i:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    if result != -1:
        ans[i - 1] += result
    else:
        ans[i - 1] += len(top)

for i in range(1, h + 1):
    start = 0
    end = len(top) - 1
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if bottom[mid] >= i:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    if result != -1:
        ans[h - i] += result
    else:
        ans[h - i] += len(top)

print(n - max(ans), ans.count(max(ans)))
