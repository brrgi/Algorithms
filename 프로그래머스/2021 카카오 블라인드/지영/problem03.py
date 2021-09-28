
LANGUAGE = {
    'cpp' : 0,
    'java' : 1,
    'python' : 2
}

PART = {
    'backend': 0,
    'frontend': 1
}
CAREER = {
    'junior': 0,
    'senior': 1
}
SOUL = {
    'pizza': 0,
    'chicken': 1
}

db = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]

def binary_search (target, l, p, c, s):
    """
        len(search_list) - start_idx = target이상의 점수를 가진 총 학생 수
    """
    
    search_list = db[l][p][c][s]
    start = 0 
    end = len(search_list)

    while (start < end):
        mid = (start + end) // 2
        if target <= search_list[mid]: end = mid
        # target 값이 현재 mid위치의 값과 같거나 큼
        else:
            start = mid + 1
    return len(search_list) - start

def solution(info, querys):
    answer = []
    
    for data in info:
        lang, part, career, soul, sc = data.split()
        db[LANGUAGE[lang]][PART[part]][CAREER[career]][SOUL[soul]].append(int(sc))
    
    for l in range(3):
        for p in range(2):
            for c in range(2):
                for s in range(2):
                    db[l][p][c][s].sort()
    

    for query in querys:
        lang, part, career, dummy = query.split(' and ')
        soul, sc = dummy.split()

        cnt = 0
        for l in range(3):
            if lang != '-' and LANGUAGE[lang] != l: continue
            for p in range(2):
                if part != '-' and PART[part] != p: continue
                for c in range(2):
                    if career != '-' and CAREER[career] != c: continue    
                    for s in range(2):
                        if soul != '-' and SOUL[soul] != s: continue
                        cnt += binary_search(int(sc), l, p, c, s)
        answer.append(cnt)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], 
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))