n = int(input())
strs = input()
now = set()
start = 0
end = 0
alp = [0 for i in range(26)]
result = 0

while end < len(strs):
    if len(now) != n:
        alp[ord(strs[end]) - 97] += 1
        now.add(strs[end])
        end += 1
    else:
        if strs[end] in now:
            alp[ord(strs[end]) - 97] += 1
            end += 1
        else:
            alp[ord(strs[start]) - 97] -= 1
            if alp[ord(strs[start]) - 97] == 0:
                now.remove(strs[start])
            start += 1
    result = max(result, end - start)
print(result)
