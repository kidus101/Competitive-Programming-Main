class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sortedPiles =sorted(piles)
        
        totalCoins =0
        pileLength = len(piles)
        
        i = pileLength - 2
        j = 0
        
        while(j < pileLength/3 ):
            j += 1
            totalCoins += sortedPiles[i]
            i-=2
        return totalCoins
    
    #Time complexity:O(n)
    #Space Complexity:O(1)
       
