#한 사람이 느끼는 불쾌함 = 동아리 방의 더러움
#불쾌함의 총합 : 사람 * 동아리 방의 더러움
#동아리 방의 더러움은 a명 들어오고 나가면 a만큼 증가
#n일 중 m번만 청소한다.

#참고
#https://velog.io/@hschoi1104/BOJ-12019-%EB%8F%99%EC%95%84%EB%A6%AC%EB%B0%A9-%EC%B2%AD%EC%86%8C

n,m=map(int,input().split())
arr=[0 for i in range(102)]
a=list(map(int, input().split()))
for i in range(n):
    arr[i+1]=a[i]
dp=[[[-1 for _ in range(102)] for _ in range(12)] for _ in range(102)]


def go(now, cnt, state, dust):
    if now==n+1:
        return 0

    t=dp[now][cnt][state]
    if t!=-1:
        return t

    dp[now][cnt][state]= go(now+1, cnt, state, dust+arr[now])
    t = go(now+1, cnt, state, dust+arr[now])

    if (cnt>0):
        dp[now][cnt][state] = min(t, go(now+1, cnt-1, now, 0))
        t = min(t, go(now+1, cnt-1, now, 0))

    dp[now][cnt][state] +=arr[now]*dust
    t+=arr[now]*dust

    return t

def traceback(cnt, state):
    for i in range(1, n):
        if cnt==0:
            break
        if dp[i + 1][cnt][state] >= dp[i + 1][cnt - 1][i]:
            state=i
            print(i, end=" ")
            cnt-=1

print(go(1,m,0,0))
traceback(m,0)