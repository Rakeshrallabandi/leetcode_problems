# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l=[]
        while temp:
            l.append(temp.val)
            temp=temp.next
        for i in range(1,len(l),2):
            l[i],l[i-1]=l[i-1],l[i]
        dummy=ListNode()
        c=dummy
        for i in l:
            c.next=ListNode(i)
            c=c.next
        return dummy.next