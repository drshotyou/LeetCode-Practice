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

# v2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        length = 1
        while(current.next):
            length+=1
            current = current.next
        current = head
        length = length//2 
        for i in range(length):
            current = current.next
        return current

#v3 real fast boi
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast =  fast.next.next
        return slow