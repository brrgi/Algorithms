import re
WILDCARD = '?'

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.cnt = 0
        self.children = {}
        self.leaf = False


class Trie(object):
    def __init__(self):
        self.head = Node(None)
  # 문자열 삽입
    def insert(self, string):
        curr_node = self.head
        # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
        for char in string:
            # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node.cnt += 1
            # 같은 문자가 있으면 노드를 따로 생성하지 않고, 해당 노드로 이동
            curr_node = curr_node.children[char]

        #문자열이 끝난 지점의 노드의 data값에 해당 문자열을 입력
        curr_node.leaf = True
    # 문자열이 존재하는지 search
    def search(self, string):
        #가장 아래에 있는 노드에서 부터 탐색 시작
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
        #탐색이 끝난 후 해당 노드의 data값이 존재한다면
        #문자가 포함되어있다는 뜻이다.
        return curr_node.cnt if curr_node.cnt else 0


def remove_wildcard(string):
    ret = ''
    for char in string:
        if char == WILDCARD: continue
        ret += char

    return ret


def solution(words, queries):
    answer = []
    trie = [Trie() for _ in range(10000)]
    reverse = [Trie() for _ in range(10000)]

    for word in words:
        trie[len(word)-1].insert(word)
        reverse[len(word)-1].insert(reversed(word))

    
    for query in queries:

        if query[0] == WILDCARD:
            if query[-1] == WILDCARD:
                answer.append(trie[len(query)-1].head.cnt)
                continue


            answer.append(reverse[len(query)-1].search(reversed(remove_wildcard(query))))
            continue

        answer.append(trie[len(query)-1].search(remove_wildcard(query)))


    print(answer)

    return answer

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
