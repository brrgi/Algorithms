import sys
input=sys.stdin.readline
n = int(input())
ipt = list(map(int, input().split()))
ipt.sort()

result = abs(ipt[0]+ ipt[1]+ ipt[2])
three = [ipt[0], ipt[1], ipt[2]]

# print(result, ipt)
for i in range(n - 2):
    j = i + 1
    k = n - 1
    while j < k:
        # print("hi", i, j, k)
        total = ipt[i] + ipt[j] + ipt[k]
        if abs(total) < result:
            result = abs(total)
            three[0] = ipt[i]
            three[1] = ipt[j]
            three[2] = ipt[k]
        if total > 0:
            k -= 1
        elif total < 0:
            j += 1
        else:
            result = total
            print(ipt[i], ipt[j], ipt[k])
            exit()
print(three[0], three[1], three[2])
