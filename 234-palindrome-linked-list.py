# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        quick = head

        while quick and quick.next:
            quick = quick.next.next
            slow = slow.next
        
        newList = slow
        prev = None
        while newList:
            tmp = newList.next
            newList.next = prev
            prev = newList
            newList = tmp
        slow = head
        while prev and slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True
        