from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        checker = {}
        for i in range(len(nums)):
            if checker.get(nums[i], 0) < 2:
                nums[index] = nums[i]
                checker[nums[i]] = checker.get(nums[i], 0) + 1
                index += 1

        return index