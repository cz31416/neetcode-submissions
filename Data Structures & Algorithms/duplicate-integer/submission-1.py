class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for n in nums:
            if n in my_dict:
                my_dict[n] += 1
            else:
                my_dict[n] = 1

        for n in my_dict:
            if my_dict[n] > 1:
                return True
        
        return False