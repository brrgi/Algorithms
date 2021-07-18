n=int(input())
strings=[]
nums=set()
for i in range(10):
    nums.add(str(i))

def divide(strs):
    temp=[]
    start=''
    for c in strs:
        if start=='':
            start+=c
            continue

        if start[0] in nums:
            if c in nums:       #둘 다 숫자
                start+=c
            else:
                temp.append(start)
                start=c
        else:
            if c not in nums:       #둘 다 문자
                start+=c
            else:
                temp.append(start)
                start=c
    if start!='':
        temp.append(start)
    return temp


for _ in range(n):
    temp=input()
    strings.append(divide(temp))
print(strings)