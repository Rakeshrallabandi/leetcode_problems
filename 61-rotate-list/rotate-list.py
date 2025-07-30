# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Get length of the list
        length = 0
        temp = head
        while temp:
            temp = temp.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Step 2: Rotate right by 1, k times
        while k:
            temp = head
            prev = None
            while temp.next:
                prev = temp
                temp = temp.next

            # Detach last node and move to front
            prev.next = None
            temp.next = head
            head = temp
            k -= 1

        return head
