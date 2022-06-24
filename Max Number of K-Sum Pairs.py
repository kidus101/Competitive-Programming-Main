class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right =len(nums) - 1
        maxOperations = 0
        
        sortedNums = nums.sort()
        
        while(left < right):
            if(nums[left] +nums[right] > k):
                right -= 1
            elif(nums[left] +nums[right] < k):
                left += 1
            else:
                maxOperations += 1
                right -= 1
                left += 1
        return maxOperations 
    
        #Time:O(nlogn)
        #space:O(1)
        
