class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack1 = []
        
        for char in s:
            if char == ')':
                Stack2 = []
                poppedElement = stack1.pop()
                
                while poppedElement != '(':
                    Stack2.append(poppedElement)
                    poppedElement = stack1.pop()
                    
                stack1 += Stack2
            else:
                stack1.append(char)
                
            
        return ''.join([char for char in stack1])
    # TC:O(N) &SC:O(N)
