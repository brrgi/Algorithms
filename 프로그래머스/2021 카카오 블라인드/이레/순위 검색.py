'''
    3시 5분 -> 3시 48분 / 4시 8분 -> 4시 13분 (sort 여러 번 하는 거 미리 처리)

'''
from bisect import bisect_left, bisect_right
def solution(info, query):
    answer = []
    cond1=['cpp','java','python']
    cond2=['backend', 'frontend']
    cond3=['junior', 'senior']
    cond4=['chicken', 'pizza']


    #step 1
    dic=dict()
    for c in cond1:
        dic[c]=dict()

    #step 2
    for i in dic:
        for c in cond2:
            dic[i][c]=dict()

    #step 3
    for i in dic:
        for j in dic[i]:
            for c in cond3:
                dic[i][j][c]=dict()


    #step 4
    for i in dic:
        for j in dic[i]:
            for q in dic[i][j]:
                for c in cond4:
                    dic[i][j][q][c]=[]

    for i in info:
        a,b,c,d,e=i.split()
        dic[a][b][c][d].append(int(e))

    for i in cond1:
        for j in cond2:
            for q in cond3:
                for w in cond4:
                    dic[i][j][q][w].sort()

    for i in query:
        i=i.replace(' and','')
        a,b,c,d,e=i.split()
        e=int(e)
        check=0

        f1=[]
        f2=[]
        f3=[]
        f4=[]
        print(i)
        print()
        if a=='-':
            f1=cond1
        else:
            f1.append(a)

        if b=='-':
            f2=cond2
        else:
            f2.append(b)

        if c=='-':
            f3=cond3
        else:
            f3.append(c)

        if d=='-':
            f4=cond4
        else:
            f4.append(d)

        for i in f1:
            for j in f2:
                for q in f3:
                    for w in f4:
                        check+=len(dic[i][j][q][w])-bisect_left(dic[i][j][q][w], e)
        answer.append(check)

    return answer


info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)