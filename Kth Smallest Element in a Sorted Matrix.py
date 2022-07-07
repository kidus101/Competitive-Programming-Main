class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        tmp = []
        for i in matrix:
            tmp.extend(i)
        tmp.sort()
        
        return tmp[k-1]
    
    # Time:O(n)
    # SPace:O(1)
