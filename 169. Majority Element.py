from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        result, major = 0, 0

        for num in nums:
            if major == 0:
                result = num

            if result == num:
                major += 1
            else:
                major -= 1

        return result