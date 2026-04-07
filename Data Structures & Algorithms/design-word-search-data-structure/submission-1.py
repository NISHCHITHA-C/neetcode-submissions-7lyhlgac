class TrieNode:
    __slots__ = ('children', 'is_end')
    def __init__(self):
        self.children:dict[str, 'TrieNode'] = {}
        self.is_end : bool = False
class WordDictionary:

    def __init__(self):
        self.root  = TrieNode()      

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True        

    def search(self, word: str) -> bool:
        return self._dfs(word, 0, self.root)

    def _dfs(self, word: str, idx: int, node: TrieNode)-> bool:
        if idx == len(word):
            return node.is_end
        ch = word[idx]
        if ch != '.':
            child = node.children.get(ch)
            return child is not None and self._dfs(word, idx+1, child)
        return any(self._dfs(word, idx+1, child)for child in node.children.values())



