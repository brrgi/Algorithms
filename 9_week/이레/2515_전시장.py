from bisect import bisect_left, bisect_right
n,s=map(int, input().split())
paintings=[]
for i in range(n):
    h, c=map(int, input().split())
    paintings.append([h,c])
paintings.sort(key=lambda x : x[0])
