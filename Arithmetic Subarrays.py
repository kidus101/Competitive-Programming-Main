class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        def boolArithmetic(list):
            if len(list) <= 2:
                return True
            else:
                list.sort()
                delta = list[1]-list[0]
                for i in range(len(list)-2):
                    if delta != list[i+2]-list[i+1]:
                        return False
                return True
        result = []
        for i in range(len(l)):
            sub_list = nums[l[i]: r[i]+1]
            result.append(boolArithmetic(sub_list))
        return result
