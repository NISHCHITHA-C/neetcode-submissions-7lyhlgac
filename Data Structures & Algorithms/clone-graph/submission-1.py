"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited:dict[Node, Node] = {}
        def dfs(curr: Node)->Node:
            if curr in visited:
                return visited[curr]
            clone = Node(curr.val)
            visited[curr] = clone # its forming a key: value pair between curr node and clone node which is same to same
            for neighbour in curr.neighbors:
                clone.neighbors.append(dfs(neighbour))
            return clone
        return dfs(node)