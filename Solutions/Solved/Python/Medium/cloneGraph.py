"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        neighborMap = {}
        nodeCopyHead = Node(node.val, [])
        neighborMap[1] = nodeCopyHead
        q = []
        q.append(node)
        i = 0
        while q:
            curNode = q.pop(0)
            nodeCopy = neighborMap[curNode.val]
            nodeNeighbors = []
            for neighbor in curNode.neighbors:
                if neighbor.val not in neighborMap:
                    neighborMap[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                nodeNeighbors.append(neighborMap[neighbor.val])
            nodeCopy.neighbors = nodeNeighbors
        return nodeCopyHead

        