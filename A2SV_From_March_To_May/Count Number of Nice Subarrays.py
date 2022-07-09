class Solution:
  def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    def numberOfSubarraysAtMost(k: int) -> int:
      ans = 0
      left = 0
      right = 0

      while right <= len(nums):
        if k >= 0:
          ans += right - left
          if right == len(nums):
            break
          if nums[right] & 1:
            k -= 1
          right += 1
        else:
          if nums[left] & 1:
            k += 1
          left += 1
      return ans

    return numberOfSubarraysAtMost(k) - numberOfSubarraysAtMost(k - 1)

# Time Complexity :O(n)
#     Space Complexity :O(1)