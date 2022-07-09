class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        counter = 0
        stack = []
        
        for num in pushed:
            stack.append(num)
            while len(stack) and counter < len(popped) and stack[-1] == popped[counter]:
                stack.pop()
                counter += 1
                
        return counter == len(popped)
    
    #Time Complexity:O(n)
    
    #Space Complexit:O(n)
        