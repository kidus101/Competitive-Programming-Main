class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sortedPiles =sorted(piles)
        pileLength = len(piles)
        totalCoins =0
        
        i = pileLength - 2
        j = 0
        
        for(j < pileLength/3; j++;i-=2 ):
            totalCoins += sortedPiles[i]
        return totalCoins
        
      #Time complexity:O(n)
    #Space Complexity:O(1)       
        
    
