# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        if head==None or head.next==None:
            return None
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if fast:
            pre=head
            while slow.next.next:
                pre=pre.next
                slow=slow.next
            pre.next=pre.next.next
            
        else:
            pre=head
            while slow.next:
                pre=pre.next
                slow=slow.next
            pre.next=pre.next.next
        return head