# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        S , F = head , head.next
        while F and F.next:
            S = S.next
            F = F.next.next

        second = S.next
        prev = S.next = None

        while second:
            T = second.next
            second.next = prev
            prev = second 
            second = T
        
        fst , snd = head , prev
        while snd:
            T1 , T2 = fst.next , snd.next
            fst.next = snd
            snd.next = T1
            fst , snd = T1 , T2
