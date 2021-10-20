from collections import deque
ex=['*','+','-','/']
idx=[]
n=input()
number=deque()
op=deque()
minus=1

def cal(oper, num1, num2):
    if oper=='*':
        return num1*num2
    elif oper=='/':
        te=divmod(num1,num2)[0]
        return te
    elif oper=='+':
        return num1+num2
    else:
        return num1-num2
if n[0]=='-':
    minus=-1
    n=n[1:]


for i, val in enumerate(n):
    if val in ex:
        idx.append(i)
        op.append(val)
if len(op)==0:
    if minus==-1:
        print(int(n)*minus)
    else:
        print(int(n))
    exit()
number.append(int(n[:idx[0]])*minus)
for i in range(len(idx)-1):
    number.append(int(n[idx[i]+1:idx[i+1]]))
number.append(int(n[idx[len(idx)-1]+1:]))
# print(number)

for i in range(len(idx)):
    res1 = cal(op[0], number[0], number[1])
    res2 = cal(op[-1], number[-2], number[-1])
    if op[0]=='*' or op[0]=='/':
        if op[-1]=='*' or op[-1]=='/':  #같을때
            if res1>=res2:
                op.popleft()
                number.popleft()
                number.popleft()
                number.appendleft(res1)
            else:
                op.pop()
                number.pop()
                number.pop()
                number.append(res2)
        else:
            op.popleft()
            number.popleft()
            number.popleft()
            number.appendleft(res1)
    else:
        if op[-1] == '*' or op[-1] == '/':  #다를때
            op.pop()
            number.pop()
            number.pop()
            number.append(res2)
        else:
            if res1 >= res2:
                op.popleft()
                number.popleft()
                number.popleft()
                number.appendleft(res1)
            else:
                op.pop()
                number.pop()
                number.pop()
                number.append(res2)
    # print(number)
print(number[0])