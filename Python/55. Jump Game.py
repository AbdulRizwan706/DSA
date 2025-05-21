from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums) - 1
        result = True
        for i in range(n, -1, -1):
            if nums[i] == 0:
                result = result and self.checker(nums, i)

        return result

    def checker(self, arr, i):
        j = i-1
        while j >= 0:
            if arr[j] != 0 and  arr[j] + j > i:
                return True
            if arr[j] + j >= len(arr) -1:
                return True
            j-=1
        return False
    

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        return True

