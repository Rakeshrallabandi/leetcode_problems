# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans=[]
        temp=head
        while temp:
            ans.append(temp.val)
            temp=temp.next
        dumy=ListNode(0)
        temp=dumy
        ans.sort()
        for i in ans:
            temp.next=ListNode(i)
            temp=temp.next
        return dumy.next