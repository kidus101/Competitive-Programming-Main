class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        
        for i in range(1,len(nums)) :
            pre = nums[i - 1]
            cur = nums[i]
            
            if(pre >= cur):
                result += pre - cur + 1
                nums[i] = pre + 1
        
        return result
    
    # Time:O(nlogn)
    # Space:O(1)
