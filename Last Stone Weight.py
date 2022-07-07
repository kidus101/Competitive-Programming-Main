class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones =[ -s for s in stones ]
        heapq.heapify(stones)
         
        while len(stones) > 1 :
            first =heapq.heappop(stones) * -1
            second =heapq.heappop(stones) * -1
            difference = abs(first - second)
            heapq.heappush(stones , difference*-1)
                
                
        return -stones[0]
    
    # Time:O(nlogn)
    # Space:O(n)
