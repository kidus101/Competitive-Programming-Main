class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c =  [ (-freq , word) for word,freq in c.items() ]
        heapq.heapify(c)
        
        output =[]
        for i in range(k):
            item = heapq.heappop(c)
            output.append(item[1])
        return output
    
    # Time:O(NLOGN)
    #     Space:O(n)
