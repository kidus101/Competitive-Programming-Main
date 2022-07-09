# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #USING o(1) SPACE COMPLEXITY AND A LINKED LIST
        
        fast = head 
        slow = head
        
        while fast and fast . next:
            fast = fast.next.next
            slow= slow.next
            
        prev = None
        while slow:
            temp = slow.next
            slow . next = prev
            prev = slow
            slow = temp
            
        left , right =head , prev
        while right :
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
            
        
        #Time Complexity : O(n)
        #space Complexity: O(1)
        
        # Though Asked to Do it using arrays 
        #that is O(n) can be done as follows.
        
#         nums = []
#         while head:
#             nums .append(head.val)
#             head = head. next
            
#         leftptr , rightptr =0 , len(nums) - 1 
        
#         while leftptr < rightptr :
#             if nums[leftptr] != nums[rightptr]:
#                 return False
#             leftptr += 1
#             rightptr-= 1   
#         return True
              
    #Time Complexity : O(n)
        #space Complexity: O(n)
    
        
        
        
        
        
        
        
        
        
        
        
        
 



