N, H = map(int, input().split())
even = [] # 석순
odd = [] # 종유석
destroyed = [0 for _ in range(H+1)]
min_val = 10 ** 10 

hudles = {}

for i in range(N):
    if i % 2 == 0:
        even.append(int(input()))
    else:
        odd.append(int(input()))
# 시간 복잡도 O(log n)
even.sort()
odd.sort()

def binary(arr: list, target:int, upper: bool) -> int:
    start = 0
    end = len(arr)

    while (start < end):
        mid = (start + end) // 2
        if target == arr[mid]: 
            if upper: 
                start = mid + 1
            else: 
                end = mid
        elif target < arr[mid]: end = mid
        else: start = mid + 1
    return start

for target in range(1, H+1):
    """
        i번째 구간을 지나는 장애물 탐색
    """
    #lower bound 탐색
    destroyed[target] += len(even) - binary(even, target, False)
    #Upper bound 탐색
    destroyed[target] += len(odd) - binary(odd, H-target, True)

    #몇개인지 저장
    if not destroyed[target] in hudles:
        hudles[destroyed[target]] = 0
    hudles[destroyed[target]] += 1
    
    #최소값 엄데이트
    min_val = min(min_val, destroyed[target])

print(f"{min_val} {hudles[min_val]}")
