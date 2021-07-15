#x의 오름차순으로 정렬 -> 전 건물 중 y값이 이 건물보다 작은 것 dp 값중 최댓값 + 가중치(c)


n=int(input())
buildings=[]

for i in range(n):
    x,y,c=map(int, input().split())
    buildings.append([x,y,c])

buildings=sorted(buildings, key=lambda x : x[0])    #x로 정렬
dp1=[i[2] for i in buildings]   #가중치
dp2=[i[2] for i in buildings]   #가중치

for i in range(1, n):
    for j in range(i):
        if buildings[j][1]<buildings[i][1]:
            if dp1[i]<buildings[i][2]+dp1[j]:
                dp1[i]=buildings[i][2]+dp1[j]

for i in range(1, n):
    for j in range(i):
        if buildings[j][1]>buildings[i][1]:
            if dp2[i]<buildings[i][2]+dp2[j]:
                dp2[i]=buildings[i][2]+dp2[j]

print(max(max(dp1), max(dp2)))
