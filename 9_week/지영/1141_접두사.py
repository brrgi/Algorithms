N = int(input())
words = sorted([input() for _ in range(N)], key=lambda x: len(x))
available = [[True]*N for _ in range(N)]
incomp = [0] * N


for idx, word in enumerate(words):
    length = len(word)
    for next in range(idx+1, N):
        if word == words[next][:length]:
            available[idx][next] = False
            incomp[idx] += 1


# print(available)
answer = 0
for idx, row in enumerate(available):
    available_set = set({words[idx]})
    for idx2, col in enumerate(row):
        if idx == idx2: continue
        if not col: continue
        if incomp[idx2] == 0: available_set.add(words[idx2])
    
    answer = max(answer, len(available_set))

print(answer)
