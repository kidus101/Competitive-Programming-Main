class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        leftptr,rightptr=0 , len(nums) - 1
        i = 0
        
        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        
        while i<=rightptr:
            if nums[i]==0:
                swap(leftptr,i)
                leftptr +=1
                
            elif nums[i]==2:
                swap(i,rightptr)
                rightptr-=1
                i-=1
            i+=1
        
        
        # Time complexity: big o= nlogn