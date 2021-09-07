N, M = map(int, input().split())
artworks = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda elm: elm[0])
costs = [0] * N
lowest = artworks[0][0]

def get_idx(target, last):
    """
        return: height보다 작은 값들 중에 가장 큰 값의 인덱스 값을 반환합니다.
        upper bound 이용해 해결
    """
    start = 0 
    end = last

    while (start < end):
        mid = (start + end) // 2
        if target < artworks[mid][0]: end = mid
        # target 값이 현재 mid위치의 값과 같거나 큼
        else:
            start = mid + 1
    return start


for order, artwork in enumerate(artworks):
    height, cost =  artwork

    if height - M < lowest: 
        if costs: 
            costs[order] = max(costs[order-1], cost)
            continue
        costs[order] = cost
    
    comp_height = height - M
    idx = get_idx(comp_height, order)

    costs[order] = max(costs[order-1], costs[idx-1] + cost)

print(costs[-1])




