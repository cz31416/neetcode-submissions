class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for n in nums:
            if n in my_dict:
                return True
            else:
                my_dict[n] = 1
        
        return False