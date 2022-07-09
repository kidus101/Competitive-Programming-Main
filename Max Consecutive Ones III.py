class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
       
        left , maximum =0 , 0
        
        for right,n in enumerate(nums):
            k -= (1 - n)
            if (k < 0):
                k += (1 - nums[left])
                left += 1
                
            maximum = max(maximum , right- left +1)
                
        return maximum
    
    #Time Complexity : O(n)
    #Space Complexity:O(n)
