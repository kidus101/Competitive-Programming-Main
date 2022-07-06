class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict ={0 : 1}
        n = len(nums)
        count , preSum = 0 , 0
        
        for num in nums:
            preSum += num
            if preSum -k in dict:
                count += dict[preSum-k]
            if preSum in dict:
                dict[preSum] += 1
            else:
                dict[preSum] = 1
        
        return count
        
        # Time:O(n)
        # Space:O(n)
