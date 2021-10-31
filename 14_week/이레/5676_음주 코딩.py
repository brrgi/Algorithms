while 1:
    try:
        n,k=map(int, input().split())
        tree=(n*4)*[0]
        nodes=list(map(int, input().split()))
        answer=''
        init(0,n-1,1)
        for _ in range(k):
            lst=input().split()
            if lst[0]=='C':
                i,V=map(int, (lst[1],lst[2]))
                nodes[i-1]=pmz(V)
                update(0,n-1,1,i-1,pmz(V))
            else:
                i,j=map(int, (lst[1],lst[2]))
                res=query(0,n-1,1,i-1,j-1)
                if(res==0):answer+='0'
                elif(res>0):answer+='+'
                else:answer+='-'
        print(answer)
    except Exception:
        break