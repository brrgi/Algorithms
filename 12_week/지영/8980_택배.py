N, C = map(int,input().split())
M = int(input())


"""
    greedy의 사용 부분
    - 도착하는 순으로 정렬함으로써 먼저 도착하는 운송 경로를 먼저 탐색하도록 한다. 
    (운송되는 박스의 로테이션을 빠르게해 더 많은 박스를 수용할 수 있도록 한다.)
"""
delivery_info = [list(map(int, input().split())) for _ in range(M)]
delivery_info.sort(key=lambda x: x[1])

get = [0] * (N+1)

ret = 0
for s, e, n in delivery_info:
    max_val = max(get[s:e])


    if max_val == C:
        """
            가장 큰 값이 트럭의 최대 수용량과 같을때, 현재 시점의 박스들은 운송할 수 없음.
            왜냐하면 이미 해당 박스를 가지고 가는 중간 지점에 버스의 최대 수용량을 넘어버리기 때문
        """
        continue
    
    add_val = min(C - max_val, n)
    ret += add_val

    for point in range(s, e):
        get[point] += add_val


print(ret)