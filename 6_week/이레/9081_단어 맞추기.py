#n! / (같은 숫자 1 a!) * (같은 숫자 2 b!) *....
#a b c d e f g h i j k l n m o p q r s t u v w x y g

t=int(input())
words=[]
for i in range(t):
    words.append(list(input()))

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
for word in words:
    print("".join(get_next_word(word)))