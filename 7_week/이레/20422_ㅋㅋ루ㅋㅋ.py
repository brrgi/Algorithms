#RRKRRKRRRKRKRRKRRRR
strs=input()
k_index=[]
r=[]
check=0
for i in range(len(strs)):
    if strs[i]=='K':
        k_index.append(i)
        r.append(check)
        check=0
    else:
        check+=1
r.append(check)

print(k_index)
print(r)

#k가 0개 or 1개인 경우
if len(r)<=2:
    print(sum(r))
    exit()
