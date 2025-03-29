class Solution:
    def rev(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.rev(l1)
        l2 = self.rev(l2)

        dummy = ListNode(-1)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            ans = carry

            if l1:
                ans += l1.val
                l1 = l1.next

            if l2:
                ans += l2.val
                l2 = l2.next

            carry = ans // 10
            temp.next = ListNode(ans % 10)
            temp = temp.next

        return self.rev(dummy.next)