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

#v2 removes unnecesarry calls and/or variables
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# root left right
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodes = []
        return preOrderTraverse(root,nodes)

def preOrderTraverse(root,nodes):
    if(root):
        nodes.append(root.val)
        if(root.children):
            for i in (root.children):
                nodes = preOrderTraverse(i,nodes)
    # print(nodes)
    return nodes

#v3 No need to check for children, loop takes care of it
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# root left right
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodes = []
        return preOrderTraverse(root,nodes)
def preOrderTraverse(root,nodes):
    if root:
        nodes.append(root.val)
        for children in root.children:
            nodes = preOrderTraverse(children,nodes)
    return nodes
