"""
    문제의 핵심: 현재 시점에서 가장 적합한 주유소를 선택하는 방법
   
    연료을 최소 빈도록 채우되, 연료가 모자라지 않아야 한다. 
    -> 가장 큰 연료의 양을 채운다. 
   
    하지만 그렇다고 최대의 연료의 양만 담는 것은 문제가 있다. 왜냐면 현재 보유한 연료량으로 그 최대로 충전할 수 있는 그 지점까지 갈 수 있다는 보장을 못하기 때문
    -> 연료를 채우되, 현재 보유한 연료량으로 갈 수 있는 주유소 중 최대로 충전할 수 있는 지점만 들른다. 

    어차피 가야되는 위치까지의 거리는 정해져 있고, 그 지점까지 갈 수 있도록 연료만 있으면 된다. 즉, 주유소를 방문할때마다 그 위치까지의 거리를 뺴는 식으로 한다면 로직이 더 복잡해진다.
    
"""

import sys
input = sys.stdin.readline
import heapq

N = int(input())
station = sorted([list(map(int, input().split()))for _ in range(N)], key=lambda elm: elm[0])
# station = [list(map(int, input().split()))for _ in range(N)]
arrived, rest_fuel = map(int, input().split())
station.append([arrived, 0])

def count_charging(station, arrived, rest_fuel):
    total_charging = 0
    fuel = []

    for _, elm in enumerate(station):

        if elm[0] > rest_fuel:
            while fuel:
                rest_fuel += heapq.heappop(fuel)[1]
                total_charging += 1
                if elm[0] <= rest_fuel:
                    break
            
            if rest_fuel >= arrived: 
                return total_charging

        if elm[0] <= rest_fuel: 
            if elm[0] == arrived:
                return total_charging
            heapq.heappush(fuel, (-elm[1], elm[1]))
        else: return -1

print(count_charging(station, arrived, rest_fuel))