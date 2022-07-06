class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        N = len(arr)
        bound = 0
        output = 0
        
        for k,v in sorted(count.items(),key=lambda x:-x[1]):
            bound += v
            output += 1
            
            if (bound >= N//2): break
        return output
    
    # Time:O(n)
    # Space:O(1)
