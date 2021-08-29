#2시 16분 -> 3시 40분 (1시간 24분)
'''
    선택, 삭제, 복구
    U X : X 칸 위에 선택
    D X : X 칸 아래 선택
    C : 선택행 삭제, 바로 아래 행 선택. but! 마지막 행이 삭제되면 바로 윗행을 선택
    Z : 가장 최근에 삭제된 행 복구
'''
def solution(n, k, cmd):
    next_dic=dict()
    prev_dic=dict()
    for i in range(n+2):
        next_dic[i-1]=i
    for i in range(n+2):
        prev_dic[i-1]=i-2
    del_row=[]
    for c in cmd:
        if c[0]=='U':
            for i in range(int(c[2:])):
                k=prev_dic[k]
        elif c[0]=='D':
            for i in range(int(c[2:])):
                k=next_dic[k]
        elif c[0]=='C':
            value=[k,prev_dic[k], next_dic[k]]
            del_row.append(value)
            next_dic[prev_dic[k]]=next_dic[k]
            prev_dic[next_dic[k]]=prev_dic[k]
            if next_dic[k]==n:
                k=prev_dic[k]
            else:
                k=next_dic[k]
        else:
            data=del_row.pop()
            next_dic[data[1]]=data[0]
            prev_dic[data[2]]=data[0]
    answer = ['X' for _ in range(n)]
    start=-1
    while start<n:
        if start>=0:
            answer[start]='O'
        start=next_dic[start]
    # print(''.join(answer))
    answer=''.join(answer)
    return answer

n=8 #행 갯수
k=0 #처음 위치
cmd=["C", "C","Z","D 1", "C","C"]
print(solution(n, k, cmd))
