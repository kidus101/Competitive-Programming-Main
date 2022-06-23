class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        sortedNums = sorted(nums)
        maximumSum = sortedNums[0]
        left = 0
        right = len(sortedNums) - 1
        while left < right:
            currentSum = sortedNums[left] + sortedNums[right]
            if maximumSum < currentSum: maximumSum = currentSum
            left+=1
            right-=1
        return(maximumSum)
    
    # Time:nlogn
    # space:O(1)
