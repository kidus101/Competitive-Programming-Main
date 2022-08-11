class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0 # day we bought stock
        fast = 1 # day we sold stock
        maxProfit = 0
        
        while(fast < len(prices)):
            currentProfit = prices[fast] - prices[slow]
            if prices[slow] < prices[fast]:
                maxProfit = max(currentProfit,maxProfit)
            else:
                slow = fast
            fast += 1
        
        return maxProfit
    
    # Time:O(N) & Space:O(1)
