class TrieNode:
    __slots__ = ('word', 'count', 'children')
    def __init__(self):
        self.word: str | None = None
        self.count:int = 0 
        self.children: dic[str, 'TrieNode'] = {}
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                node.count +=1
            node.word = word
        result:list[str] = []
        rows, cols = len(board), len(board[0])
        def dfs(r:int, c:int, node: 'TrieNode')-> None:
            ch = board[r][c]
            child = node.children.get(ch)
            if child is None :
                return
            if child.word:
                result.append(child.word)
                child.word = None
                child.count -= 1
            board[r][c] = '#'
            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0<=nc <cols and board[nr][nc] != '#':
                    dfs(nr, nc, child)
            board[r][c] = ch
            if child.count == 0:
                del node.children[ch]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in root.children:
                    dfs(row, col, root)
        return result