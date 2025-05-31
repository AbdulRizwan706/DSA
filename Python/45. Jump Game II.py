class Solution:
    def jump(self, nums: List[int]) -> int:
        far, cur_idx, count = 0, 0, 0

        for i in range(len(nums)-1):
            far = max(far, i + nums[i])
            if i == cur_idx:
                count += 1
                cur_idx = far
        return count


        