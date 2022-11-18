# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        found = set()
        
        while current:
            if current in found: return current
            found.add(current)
            current = current.next
        return None

#v2 better than 94%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        copy = head
        nodesList = []
        while copy:
            nodesList.append(copy)
            copy = copy.next
            length+=1
        return nodesList[length//2]
        