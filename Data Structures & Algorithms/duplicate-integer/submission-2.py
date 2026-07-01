class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Input is a list of integer
        #Return True if a value appears more than once
        #We can use a list to store the item and check any incoming value existed
        #
        all_items = []
        for num in nums:
            if len(all_items) == 0:
                all_items.append(num)
                continue
            if num in all_items:
                return True
            all_items.append(num)
        return False
        #Then second time we iterate we check if 