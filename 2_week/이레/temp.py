from functools import cmp_to_key

n=int(input())
strings=[]
nums=set()
for i in range(10):
    nums.add(str(i))

alp=dict()
for i in range(26):
    alp[chr(65+i)]=2*i
    alp[chr(97+i)]=2*i+1
# print(alp)
#0123456789 AaBbCcXx...Zz

def count_zero(number):
    val=0
    for i in range(len(number)):
        if number[i]=='0':
            val+=1
        else:
            break
    return val

def compare(a,b):       #a가 더 큰 경우 위치를 바꿔서 계속 비교를 진행하는 함수
    a_length=len(a)
    b_length=len(b)

    for i in range(min(a_length, b_length)):
        if a[i].isdigit():  #a문자는 숫자일 때
            if b[i].isdigit():  #a숫자 b숫자
                if int(a[i])<int(b[i]):
                    return -1
                elif int(a[i])>int(b[i]):
                    return 1
                else:       #같을 때 -> 0이 붙어있는거를 확인해야 한다.
                    if count_zero(a[i])<=count_zero(b[i]):
                        return -1
                    else:
                        return 1
            else:               #a숫자 b문자
                return -1
        else:
            if b[i].isdigit():  #a문자 b숫자
                return 1
            else:               #a문자 b문자
                for j in range(min(len(a[i]), len(b[i]))):
                    if alp[a[i][j]]==alp[b[i][j]]:
                        continue
                    elif alp[a[i][j]]<alp[b[i][j]]:
                        return -1
                    else:
                        return 1

                if len(a[i])<len(b[i]):
                    return -1
                elif len(a[i])>len(b[i]):
                    return 1
                else:
                    continue
    if a_length<=b_length:
        return -1
    else:
        return 1

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

# for i in range(n-1):
#     for j in range(i+1, n):
#         if compare(strings[i],strings[j])==-1:
#             continue
#         else:
#             strings[i], strings[j]=strings[j], strings[i]
# print(strings)
# for i in strings:
#     print("".join(i))
# print("------")
strings = sorted(strings, key=cmp_to_key(compare))

for i in strings:
    print("".join(i))