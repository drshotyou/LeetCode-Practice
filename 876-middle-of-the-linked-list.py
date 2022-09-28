# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head;
        length = 1;
        while(temp.next):
            length+=1
            temp = temp.next
        # print (head)
        # print (length)
        # print (temp)
        if(length % 2 != 0):
            target = ceil(length / 2)
            # print(target)
        else:
            target = (length/2) + 1
        temp = head
        while(target>1):
            temp = temp.next
            target-=1
        # print(temp)
        return temp