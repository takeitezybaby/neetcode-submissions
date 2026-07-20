# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
   
        if not list1: return list2
        if not list2: return list1

        if list1.val <= list2.val:
            head = tail = list1
            curr1, curr2 = list1.next, list2
        else:
            head = tail = list2
            curr1, curr2 = list1, list2.next

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        tail.next = curr1 or curr2
        return head