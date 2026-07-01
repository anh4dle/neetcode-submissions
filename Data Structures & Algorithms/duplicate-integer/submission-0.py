class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_map = {}
        for num in nums:
            if num in h_map:
                return True
            h_map[num] = 1
        return False