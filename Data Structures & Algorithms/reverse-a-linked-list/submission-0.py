# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr , prev = head , None
        while curr:
            nxt = curr.next
            curr.next = prev # reverse the link now prev -> 1 -> None
            prev = curr
            curr = nxt
        return prev

