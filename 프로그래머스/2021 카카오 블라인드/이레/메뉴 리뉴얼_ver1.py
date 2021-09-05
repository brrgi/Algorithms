from itertools import combinations
'''
2시->3시// 4시 14분->4시 18분 
    orders는 최대 20개
    단품메뉴는 A~Z
    가장 많이 함께 주문한 단품메뉴 -> 코스요리(최소 2가지 이상)
'''

bits=set()
def solution(orders, course):
    global bits
    alp = [chr(65 + i) for i in range(26)]
    answer = []
    for i in course:
        bits=set()
        temps = []
        t = list(combinations(alp, i))
        visit=[0 for i in range(26)]
        bitmask(0, visit, 0, i)
        max_length = 0
        res = []
        for temp in bits:
            check = 0
            for order in orders:
                tt=strToBinary(order)
                if tt&temp == temp:
                    check += 1
            if check >= 2:
                if max_length == check:
                    res.append(binToStr(temp))
                elif max_length < check:
                    res = []
                    max_length=check
                    res.append(binToStr(temp))
        answer += res

    for r in range(len(answer)):
        answer[r]=''.join(answer[r])
    answer.sort()
    return answer

def bitmask(value, visit,n, last):
    global bits
    if n==last:
        return bits.add(value)

    for i in range(26):
        if visit[i]==0:
            visit[i]=1
            bitmask(value|1<<i, visit, n+1, last)
            visit[i]=0


def strToBinary(strs):
    value=0
    for i in strs:
        value|=1<<(ord(i)-65)
    return value

def binToStr(bi):
    s=''
    start=0
    for i in range(26):
        if bi&1<<i==1<<i:
            s+=chr(65+i)
    return s


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))
