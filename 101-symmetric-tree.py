class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftQueue = deque()
        rightQueue = deque()
        leftQueue.append(root.left)
        rightQueue.append(root.right)

        while leftQueue and rightQueue:
            left = leftQueue.popleft()
            right = leftQueue.popleft()
            if (left and right and left.val == left.right):
                leftQueue.append(left.left)
                leftQueue.append(left.right)
                rightQueue.append(right.left)
                rightQueue.append(right.right)
            elif (not left and not right):
                continue
            else:
                return False
        return True