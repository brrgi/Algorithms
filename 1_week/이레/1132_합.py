visit=[0 for i in range(10)]
zero=[0 for i in range(10)]

n=int(input())
dic=dict()
for i in range(10):
    dic[chr(65+i)]=0

checking=0
alp=[]
for i in range(n):
    t=input()
    zero[ord(t[0])-65]=1
    alp.append(t)
    t=t[::-1]
    for j in range(len(t)):
        visit[ord(t[j])-65]+=1*(10**j)
    # print(visit)
# print(visit)    #사용된 것 자릿 수 체크
# print(zero)     #맨 앞자리에 사용된 것 체크
if visit.count(0)==0:
    checking=1

#0은 사용된 것 중 제일 작은 값부터 맨 앞자리가 사용안된 것 0으로 처리
test=[]
for i in range(10):
    if zero[i]==0:
        if visit[i]!=0:
            test.append((i,visit[i]))


test=sorted(test, key=lambda x:x[1])
# print(test)
# print("확인", test[0])
if checking == 1:
    dic[chr(65+test[0][0])]=0
    visit[test[0][0]]=0

start=9
while visit.count(0)!=10:
    k=visit.index(max(visit))
    dic[chr(65+k)]=start
    start-=1
    visit[k]=0

for i in range(n):
    for j in range(10):
        alp[i]=alp[i].replace(chr(65+j), str(dic[chr(65+j)]))
# print(alp)
alp=list(map(int, alp))
print(sum(alp))
