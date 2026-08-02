# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head :
            return []
        length = 1
        temp = head
        while temp.next :
            temp = temp.next
            length += 1
        i = length - n 
        curr, prev = head, None
        if i > 0 :
            for j in range(i) :
                prev = curr
                curr =  curr.next
            prev.next = curr.next
            curr.next = None
            return head
        else : 
            temp = curr.next
            curr.next = None
            return temp