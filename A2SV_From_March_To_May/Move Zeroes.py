class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    j = 0
    for num in nums:
      if num != 0:
        nums[j] = num
        j += 1

    for i in range(j, len(nums)):
      nums[i] = 0

# Time: O(n)
# Space: O(1)







    