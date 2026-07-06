class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i ,num_0 in enumerate(nums):
            result[i] = 1
            for j, num_1 in enumerate(nums):
                if i == j:
                    continue
                result[i] *= num_1
        return result