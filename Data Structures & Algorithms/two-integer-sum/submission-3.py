class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        answer = []
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if b in new_dict:
                answer.append(new_dict[b])
                answer.append(i)
                answer.sort()
                return answer
            else:
                new_dict[a] = i