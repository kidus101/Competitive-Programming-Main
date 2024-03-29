class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        sortedNums = sorted(nums)
        dic = {}
        result = []
	
        for i in range(len(sortedNums)):
            if sortedNums[i] not in dic:
                dic[sortedNums[i]] = i
                
        for i in nums:
            result.append(dic[i])
        return result
    
    # Time:O(N)
    # Space:O(1)
