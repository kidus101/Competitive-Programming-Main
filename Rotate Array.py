class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
     
        def reverse(nums , left , right):
            while(left < right):
                nums[left] , nums[right] = nums[right], nums[left] 
                left += 1
                right -= 1
        k  = k % len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        
        # Time: O(1)
        # Space:O(1)
       
      
        
