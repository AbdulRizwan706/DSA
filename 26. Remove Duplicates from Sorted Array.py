class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0

        remember_set = set()
        for i in range(len(nums)):
            if nums[i] not in remember_set:
                nums[index] = nums[i]
                remember_set.add(nums[i])
                index += 1

        return index
        