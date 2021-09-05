#1시 40분 -> 2시
def solution(new_id):
    answer = ''
    alps=[chr(i+97) for i in range(26)]
    numbers=[str(i) for i in range(10)]
    chars=['-','_','.']
    #step 1
    new_id=new_id.lower()
    print(new_id)
    #step 2
    temp=''
    for s in new_id:
        if s not in alps+numbers+chars:
            continue
        temp+=s
    new_id=temp
    print(new_id)
    #step 3
    temp=''
    check=0
    for s in new_id:
        if s=='.':
            check+=1
            if check==2:
                check=1
                continue
        else:
            check=0
        temp+=s
    new_id=temp
    print(new_id)
    #step 4
    if new_id[0]=='.' and new_id[-1]=='.':
        new_id=new_id[1:len(new_id)-1]
    elif new_id[0]=='.':
        new_id=new_id[1:]
    elif new_id[-1]=='.':
        new_id=new_id[:len(new_id)-1]
    print(new_id)
    #step 5
    if len(new_id)==0:
        new_id='a'
    print(new_id)
    #step 6
    if len(new_id)>=16:
        new_id=new_id[:15]
    if new_id[-1]=='.':
        new_id=new_id[:14]
    print(new_id)
    #step 7
    if len(new_id)<=2:
        new_id=new_id+(3-len(new_id))*new_id[-1]
    print(new_id)
    answer=new_id
    return answer


new_id="123_.def"
print(solution(new_id))