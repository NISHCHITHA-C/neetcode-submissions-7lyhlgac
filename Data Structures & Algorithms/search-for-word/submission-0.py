class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import Counter
        m, n = len(board), len(board[0])
        board_count = Counter(board[i][j] for i in range(m) for j in range(n))
        word_count = Counter(word)
        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        def dfs(r: int, c:int, idx:int):
            if idx == len(word):
                return True
            if r<0 or r>= m or c<0 or c>=n:
                return False
            if board[r][c] != word[idx]:
                return False
            temp, board[r][c] = board[r][c], '#'
            found = (dfs(r-1, c, idx+ 1) or 
                dfs(r+1, c,idx + 1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1))
            board[r][c] = temp
            return found
        return any(dfs(r,c, 0) for r in range(m) for c in range(n) if board[r][c] == word[0])


        