class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #
        prefix_prod = [1] * len(nums)
        suffix_prod = [1] * len(nums)
        result = [1] * len(nums)
        #Build prefix prod of current index
        for i, num in enumerate(nums):
            if i > 0:
                #Prefix prod of cur is index
                #cur num * previous prod
                prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        print("Showing prefix", prefix_prod)
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1:
                suffix_prod[i] = suffix_prod[i+1] * nums[i+1]
            result[i] = prefix_prod[i] * suffix_prod[i]
        return result