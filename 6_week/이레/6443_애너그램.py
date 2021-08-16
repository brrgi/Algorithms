import sys
from itertools import permutations
input=sys.stdin.readline
n = int(input())

def get_next_word(word):
    i=len(word)-2
    while i>=0 and word[i]>=word[i+1]:
        i-=1
    if i==-1:
        return word

    j=len(word)-1
    while word[i]>=word[j]:
        j-=1

    word[i], word[j] = word[j], word[i]

    temp=word[:i+1]
    temp=temp+list(reversed(word[i+1:]))

    return temp


for _ in range(n):
    ipt = sorted(input().rstrip())
    print("".join(ipt))
    while 1:
        t=get_next_word(list(ipt))
        if "".join(t)==ipt:
            break
        print("".join(t))
        ipt="".join(t)