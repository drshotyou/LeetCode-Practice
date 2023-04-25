class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if not head or not head.next:
           return head
       mid = self.midPoint(head)
       left = self.sortList(head)
       right = self.sortList(mid)

       return self.merge(left,right)
    
    def midPoint(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(left,right):
        dummy = ListNode(0)
        current = dummy
        while left and right:
            if left.val < right.val:
                current.next = left
                current = current.nexts
                left = left.next
            else:
                current.next = right
                current = current.next
                right = right.next
        current.next = left or right
        return dummy.next
        
