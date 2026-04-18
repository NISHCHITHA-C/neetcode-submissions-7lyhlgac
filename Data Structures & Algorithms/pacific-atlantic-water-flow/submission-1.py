class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        dirs = ((1,0),(-1,0), (0,1), (0,-1))
        from collections import deque
        def bfs(seeds:List[tuple[int,int]])->List[tuple[int,int]]:
            visited:set[tuple[int,int]] = set(seeds)
            queue:deque[tuple[int,int]] = deque(seeds)
            while queue:
                r,c = queue.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if (
                        0<=nr < m
                        and 0<= nc < n
                        and heights[nr][nc] >= heights[r][c]
                        and (nr, nc) not in visited
                        ):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return visited
        pacific_seeds = [(r,0) for r in range(m)] + [(0,c) for c in range(1,n)]
        atlantic_seeds = [(r, n-1) for r in range(m)] + [ (m-1, c) for c in range(n -1)]
        pacific_reach = bfs(pacific_seeds)
        atlantic_reach = bfs(atlantic_seeds)
        return [[r,c] for r,c in pacific_reach & atlantic_reach]
        