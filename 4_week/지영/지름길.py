num, arrived = map(int, input().split())
min_val = [0 for _ in range(arrived+1)]
shortcuts = [list(map(int, input().split())) for _ in range(num)]

# 도착 지점까지 1km 당 조회
for dist in range(1, arrived + 1):
    # 바로 직전 값에서 현재 지점까지 1km 추가
    min_val[dist] = min_val[dist-1]+1
    # 현재 위치에서 업데이트할 지름길이 있는지 조회
    for shortcut in shortcuts:
        # 종착지를 기준으로 비교 [지름길을 이용하지 않고 쭉 일직선으로 현재 지점까지 왔을 떄 거리, 
        # 지름길을 이요했을 때의 거리[시작지점의 최소값 + 지름길의 거리]]
        if dist == shortcut[1]:
            min_val[dist] = min(min_val[dist], min_val[shortcut[0]] + shortcut[2])

print(min_val[arrived])