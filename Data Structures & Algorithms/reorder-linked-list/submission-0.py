# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # divide into two lists
        first = head
        second = slow.next
        slow.next = None

        # reverse the second list
        before = None
        current = second
        while current:
            after = current.next
            current.next = before
            before = current
            current = after
        
        second = before
        first = head

        #merge both lists
        while second:
            tmp1 = first.next
            tmp2 = second.next
            
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
            
        
