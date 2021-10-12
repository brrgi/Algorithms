n=int(input())
stack=[]
max_val=1000000000

# direction=[0]*(2*max_val+10)      #(=1 )=-1

px, py = map(int, input().split())
print(px,py)
px, py = map(int, input().split())
print(px,py)
for i in range(n-2):
    x, y = map(int, input().split())
    #
    # if i%2==0:  #양 옆
    #     direction[max_val+x]
    # else:       #위 아래
