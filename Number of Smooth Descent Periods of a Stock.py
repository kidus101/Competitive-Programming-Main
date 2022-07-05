class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        start,end =0,0
        count = 1
        
        for end in range(1,len(prices)):
            if (prices[end] == prices[end-1] - 1):
                count += end - start + 1
            else:
                start = end
                count += end - start + 1
        return count
    # Time:O(n)
    # Space:O(1)
