from collections import defaultdict
from bisect import bisect_right

def count_valid_indices(word_indices, word_index) -> int:
    return bisect_right(word_indices, word_index)

word_idx = {}

class Node:
    def __init__(self):
        self.children: dict[Node] = defaultdict(lambda: Node())
        self.word_indices: list[int] = []

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        current: Node = self.root
        word_index = word_idx[word]
        current.word_indices.append(word_index)

        for char in word:
            current = current.children[char]
            current.word_indices.append(word_index)

    def count_thingies(self, query) -> int:
        word_index = word_idx[query] if query in word_idx else float('inf')        
        current = self.root
        count = count_valid_indices(current.word_indices, word_index)

        for char in query:
            if len(current.children) == 0:
                break
            else:
                current = current.children[char]
            
            count += count_valid_indices(current.word_indices, word_index)

        return count
    
trie = Trie()

for index in range(int(input())):
    word = input()
    word_idx[word] = index
    trie.insert(word)

for _ in range(int(input())):
    query = input()
    print(trie.count_thingies(query))