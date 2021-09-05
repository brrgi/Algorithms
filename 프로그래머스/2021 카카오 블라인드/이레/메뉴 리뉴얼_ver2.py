#2시->3시// 4시 14분->4시 45분
from itertools import combinations
def solution(orders, course):
    answer = []
    orders.sort(key=lambda x : len(x))
    dic=dict()
    res=[[] for _ in range(len(course))]
    for i in range(len(course)):
        dic[course[i]]=[i,0]    #인덱스 벨류
    setC=set(course)
    for i in range(len(orders)):
        for j in range(2, len(orders[i])+1):
            comb = combinations(orders[i], j)
            for w in comb:
                check = 1
                cw=''.join(w)
                for q in range(i+1, len(orders)):
                    if set(cw).intersection(set(orders[q]))==set(cw):
                        check+=1
                if len(w) not in setC:
                    continue
                if check==1:
                    continue
                if dic[len(w)][1]==check:
                    res[dic[len(w)][0]].append(cw)
                elif dic[len(w)][1]<check:
                    res[dic[len(w)][0]]=[cw]
                    dic[len(w)][1]=check
    # print(res)
    for i in range(len(course)):
        for j in res[i]:
            answer.append(''.join(sorted(list(j))))
    answer.sort()
    return answer


orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
