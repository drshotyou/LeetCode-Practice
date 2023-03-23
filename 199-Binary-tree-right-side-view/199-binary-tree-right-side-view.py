# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        rightSide = []
        q =  deque([root])

        while q:
            last = None
            qLen =  len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    last = node
                    q.append(node.left)
                    q.append(node.right)
            if last:
                rightSide.append(last.val)
        return rightSide