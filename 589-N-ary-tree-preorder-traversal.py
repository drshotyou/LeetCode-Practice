"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output =  []
        current = root
        output = traverse(current,output)
        return output
        
def traverse(root,output):
    if root:
        output.append(root.val)
        if(root.children):
            for i in range(len(root.children)):
                output = traverse(root.children[i],output)
    return output