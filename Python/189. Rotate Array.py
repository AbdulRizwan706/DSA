from typing import List

## two edge cases k = k%(len(nums)) and if len(nums) <= 1 return nums

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        k = k%(len(nums))
        n = len(nums) - 1
        self.rev_arr(nums, 0, n)
        self.rev_arr(nums, 0, k-1)
        self.rev_arr(nums, k, n)

    def rev_arr(self, nums, i, j):
        while j > i:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1