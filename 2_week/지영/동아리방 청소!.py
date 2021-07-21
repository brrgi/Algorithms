N, M = map(int, input().split())
dirtiness_degree = list(map(int, input().split()))
dirtiness_degree.insert(0,0)

memoization = [[[-1 for _ in range(N+1)] for _ in range(M+1)] for _ in  range(N+1)]

def visited(days, discomfort, last, clear_count):
    """
        [params]
        - days: 현 날짜
        - discomfort: 누적된 불편함
        - last: 마지막으로 청소한 일자
        - clear_count: 청소 수
    """ 
    if days == N+1: return 0
    if memoization[days][clear_count][last] != -1:
       return memoization[days][clear_count][last]

    #이날 청소를 하지 않았거나 했다고 가정했을 때, 그 다음 일어날 일들의 최소값
    ret = visited(days + 1, discomfort + dirtiness_degree[days], last, clear_count)
    #청소를 한 경우와 청소하지 않은 경우의 최소 값 비교
    if clear_count < M: ret = min(ret, visited(days + 1, 0, days, clear_count + 1))

    #이날 이후에 한 값에서 현재 추가해야할 값 추가
    ret += dirtiness_degree[days] * discomfort
    memoization[days][clear_count][last] = ret
    return ret

#역추적 출력
def traceback(clear_count, last): 
    for i in  range(1, N):
        if clear_count >= M:
            break
        if memoization[i + 1][clear_count][last] >= memoization[i + 1][clear_count + 1][i]:
            last = i
            print(i)
            clear_count += 1

print(visited(1,0,0,0))
traceback(0,0)