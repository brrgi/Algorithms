n=int(input())
strs=[input() for _ in range(n)]
strs.sort()
dic=dict()
for s in strs:
    dic[s]=0
result=0

class Node():
    def __init__(self,key,data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie():
    def __init__(self):
        self.head=Node(None)

    '''
        트라이에 문자열을 삽입
    '''
    def insert(self, string):
        global result, dic
        curr_node=self.head
        for char in string:         #a b c d
            if char not in curr_node.children:
                curr_node.children[char]=Node(char)
            curr_node=curr_node.children[char]
            if curr_node.data!=None:
                dic[curr_node.data]=0
        curr_node.data=string
        dic[curr_node.data]=1

t=Trie()
for s in strs:
    t.insert(s)

result=0
for i in dic:
    result+=dic[i]
print(result)