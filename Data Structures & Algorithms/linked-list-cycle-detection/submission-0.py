# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise , rabbit = head , head

        while rabbit and rabbit.next:
            tortoise = tortoise.next
            rabbit = rabbit.next.next
 # for every T the R will run twice so if these is a loop it both will meet again otherwise not           
            if tortoise == rabbit: 
                return True
        return False