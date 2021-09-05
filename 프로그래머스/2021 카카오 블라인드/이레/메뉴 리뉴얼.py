from itertools import combinations

'''
2시-> 2시 25분
    orders는 최대 20개
    단품메뉴는 A~Z
    가장 많이 함께 주문한 단품메뉴 -> 코스요리(최소 2가지 이상)
'''


def solution(orders, course):
    alp = [chr(65 + i) for i in range(26)]
    temps = []
    answer = []
    for i in course:
        temps = []
        t = list(combinations(alp, i))
        for j in t:
            temps.append(''.join(j))

        max_length = 0
        res = []
        for temp in temps:
            check = 0
            for order in orders:
                if set(temp).intersection(set(order)) == set(temp):
                    check += 1
            if check >= 2:
                if max_length == check:
                    res.append(list(''.join(temp)))
                elif max_length < check:
                    res = []
                    max_length=check
                    res.append(list(''.join(temp)))
        answer += res

    for r in range(len(answer)):
        answer[r]=''.join(answer[r])
    answer.sort()
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
