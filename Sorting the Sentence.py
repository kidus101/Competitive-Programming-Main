class Solution: 
    def sortSentence(self, s: str) -> str: 
        dic = {} 
        for i in s.split(): 
            dic[i[-1]] = i[:-1] 
            
        output = [] 
        for num, word in sorted(dic.items()): 
            output.append(word) 
            
        return " ".join(output)
    
    # Time:O(N)
    # Space:O(1)
