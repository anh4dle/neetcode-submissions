class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Unknown: indexes of 2 number
        Data: 
        - list of integer, an an integer called target
        - find index of 2 number have sum equal target        
        - Assume that the array is not sorted
        Condition:
        - can't sort because it will change index
        Algo:
        Use a dict to store all num
        Traverse list and store all num in a dict
        Traverse list again to check if there's exist a number x in dict
        that target - current_number in list = x
        """
        _dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in _dict and i > 0:
                if _dict[diff] != i:
                    if i < _dict[diff]:
                        return [i, _dict[diff]]
                    else:
                        return [_dict[diff], i]
            _dict[num] = i
            
        return [-1,-1]