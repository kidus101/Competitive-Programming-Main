class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        sortedN = sorted(i+1 for i in range(n))
        
        current = len(sortedN)-1
        
        while len(sortedN)>1:
            current = (current+k)%len(sortedN)
            sortedN.remove(sortedN[current])
            current-=1
            current%=len(sortedN)
        return sortedN[0]
