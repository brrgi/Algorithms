from itertools import combinations
import heapq

def solution(orders, course):
    answer = []
    # course 개수만큼 끊어야됨.
    for bundle in course:
        hash_map = {}
        max_val = 0
        for order in orders:
            for item in combinations(order, bundle):
                string = ''.join(sorted(item))
                if string not in hash_map.keys():
                        hash_map[string] = 0
                hash_map[string] += 1
        
        rets = []
        for key in hash_map.keys():
            if hash_map[key] < 2: continue

            if max_val < hash_map[key]:
                rets = [key]
                max_val = hash_map[key]
                continue
                
            if max_val == hash_map[key]:
                rets.append(key)
                continue
        
        for ret in rets:
            answer.append(ret)
        
    answer.sort()
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))