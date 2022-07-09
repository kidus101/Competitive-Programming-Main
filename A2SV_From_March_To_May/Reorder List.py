# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slowptr,fastptr = head,head.next
        
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next

            
        secondptr = slowptr.next
        prev = slowptr.next = None
        while secondptr:
            tmp = secondptr.next
            secondptr.next = prev
            prev = secondptr
            secondptr = tmp
            
        firstptr , secondptr = head, prev
        while secondptr:
            tmp1, tmp2 = firstptr.next , secondptr.next
            firstptr.next = secondptr
            secondptr.next = tmp1
            firstptr , secondptr =tmp1 , tmp2

            
            #Time complexity : O(n)
            # Space Complexity : O(1)